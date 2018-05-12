'''
    Written by: 
        Debojit Kaushik (May 2018)
        Sandeep Joshi (May 2018)
'''

from StageExtractor import EntityExtractor
import pprint
from shlex import shlex
import os
import re
import sys
import traceback
from functools import reduce
import statistics
import pygal
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from keras.preprocessing.text import text_to_word_sequence
import numpy as np
import logging
from cluster import verbose_print


#Logging setup
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "info.log",
    level=os.environ.get("LOGLEVEL", "INFO"),
    format = LOG_FORMAT,
    filemode = 'w')
log = logging.getLogger(__name__)



class Statistics:
    '''
        Class with different methods of analytics methods for JenkinsFiles written in groovy.
    '''

    def __init__(self):
        log.info("Statistics instance Created.") 
        self.avg_timeout = 0
        self.timeouts = []
        self.timeout_std_dev = 0
        self.timeout_variance = 0

    def get_post_block_data(self,filepath):
        extractor = EntityExtractor()
        elements = extractor.get_elements(filepath)

        post_content = extractor.get_all_entities(elements,'post','post',False)
        post_block_names = ['always','success','failure']

        post_elem_dict = []
        for name in post_block_names:
            post_dict = extractor.get_all_entities(post_content,name,name,True)
            
            post_elem_dict.append(post_dict)
        final_dict = {}
        for d in post_elem_dict:
            for key in d.keys():
                final_dict[key] = d[key]
        return final_dict
    

    def build_tool_stats(self, path):
        """
            Method to analysis frequencies of different build tools being used over the dataset.
        """
        try:
            os.chdir(path)
            log.info("build_tool_stats called. Changing directory to %s" %(os.getcwd()))
            files = os.listdir()

            #Frequency dictionary to keep a track fo which of the following build tools occer how many times.
            build_tools = {
                'webpack':0,
                'cmake':0,
                'gradle':0,
                'gradlew':0,
                'mvn':0,
                'ant':0,
                'maven':0,
                'msbuild':0,
                'make':0,
                'sbt':0,
                'hudson':0
            }

            # For every jenkins file in the dataset, create shlex blob and compare for every build tool in the it.
            # If Yes, then increment frequency.Regex used here to capture any occurrence rather than string comparison.
            for item in list(files):
                try:
                    consolidated = reduce(lambda x, y: x+' '+y, list(shlex(open(item))))
                    for it in list(build_tools.keys()):
                        #Regex which accepts form of [anything except letters]build_tool_name[space].
                        result = re.findall(r'[^a-zA-Z]+%s\s'%(it), consolidated)
                        if result:
                            build_tools[it] += 1      
                except Exception as e:
                    log.info(e)
                    continue
            verbose_print('Build Tools:')
            print(build_tools)
            
            #Creating a pie chart with the frequncies.
            pie_chart = pygal.Pie()
            pie_chart.title = 'Build tools usage over %s files' %(len(files))
            # For every build tool add frequency to pie chart.
            for item in build_tools:
                pie_chart.add(item, build_tools[item])
            pie_chart.render_to_file("../../build_tools.svg")
            
            #Switch back to root directory to further call methods.
            os.chdir('../..')
        except Exception:
            log.info(traceback.format_exc())
    
    def get_timeout_stats(self, path):
        try:
            # Go down to the dataset directory.
            os.chdir(path)
            files = os.listdir()
            log.info("Changed to directory %s" %(os.getcwd()))

            # For every jenkins file check if 'timeout' occurs in the file.
            # If yes, the gather the next occurring integer as the time out quantity, and abort search if integer not found.
            for item in list(files):
                try:
                    if 'timeout' in list(shlex(open(item))):
                        temp = list(shlex(open(item)))
                        #Check for an integer for the next 5 indices from the current index.
                        for it in temp[temp.index('timeout'):temp.index('timeout')+5]:
                            if it.isdigit() and float(it) < 1000:
                                self.timeouts.append(float(temp[temp.index(it)]))
                                break
                except Exception:
                    log.info(traceback.format_exc())

            self.avg_timeout = sum(self.timeouts)/len(self.timeouts)
            self.timeout_std_dev = statistics.stdev(self.timeouts)
            
            verbose_print("Timeouts:")
            print(self.timeouts)
            verbose_print("Std Dev of timeouts:") 
            print(self.timeout_std_dev)
            verbose_print("Avg timeout:")
            print(self.avg_timeout)
            verbose_print("% of files with timeouts: ")
            print(100*len(self.timeouts)/len(files), '%')

            os.chdir('../..')
            log.info("Changed back to directory %s" %(os.getcwd()))
        except Exception:
            log.info(traceback.format_exc())


    def build_word_cloud_high_level(self, path):
        try:
            extractor = EntityExtractor()
            os.chdir(path)
            log.info("Changing to directory %s" %(os.getcwd()))
            files = os.listdir()
            
            #Variable which will hold the complete string blob of the corpus.
            consolidated_text = ''
            for item in files:
                try:
                    elems = list(shlex(open(item)))
                    # Extracts the 'stage' or specified level of sugar fro the shlex output. Keys contains the job being done.
                    extract_keys = list(extractor.get_all_entities(elems,'stage', None, True).keys())
                    if extract_keys:
                        #Clean the extract for unwanted characters.
                        temp_string = ' '.join([a.lower().strip().replace("'", "").replace('"', '').replace('-', '') for a in extract_keys])
                        consolidated_text += temp_string
                except Exception:
                    log.info(traceback.format_exc())
            # Regex removes bad characters like \uXXXX.
            consolidated_text = re.sub(r"[\\]u[0-9]+", "", consolidated_text)
            # Write to a graphic file, worlcloud.
            self.create_word_cloud(
                consolidated_text, 
                "'Stage' arguments/processes", 
                file_path = '/Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/stage_word_cloud.png')
            log.info("Created graphic file in project root directory")

            os.chdir('../..')
            log.info("Change to direcotry %s" %(os.getcwd()))
        except Exception:
            log.info(traceback.format_exc())

    def create_word_cloud(self, text, title ,file_path = None, show = False):
        try:
            log.info("Graphics file about to be created %s %s" %(title, file_path))
            #Create word clooud objects with the set parameters.
            wc = WordCloud(background_color = "white", height = 400, width = 600,scale = 3, max_words = 1000, margin=10,random_state=1).generate(text)
            default_colors = wc.to_array()
            
            plt.axis("off")
            if file_path:
                wc.to_file(file_path)
            plt.title(title)
            plt.imshow(default_colors, interpolation="bilinear")
            plt.axis("off")
            if show:
                plt.show()
        except Exception:
            log.info(traceback.format_exc())
    
    def build_word_cloud_low_level(self, path):
        try:
            extract = EntityExtractor()
            os.chdir(path)
            log.info("Changing to directory %s" %(os.getcwd()))
            files = os.listdir()
            
            #Variable which will hold the complete string blob of the corpus.
            consolidated_text = ''
            for item in files:
                try:
                    elems = list(shlex(open(item)))
                    # Extracts the 'stage' or specified level of sugar from the shlex output. 
                    # Values contains the co routine being performed within this block..
                    f = list(extract.get_all_entities(elems,'stage', None, True).values())
                    
                    #Consolidates a list of list of strings into a single string.
                    temp = ' '.join([' '.join(item) for item in f])
                    consolidated_text += temp
                except Exception:
                    continue
            #Further cleaning of the string with removal of bad characters.
            consolidated_text = text_to_word_sequence(consolidated_text)
            consolidated_text = ' '.join(consolidated_text).replace("'", "").replace('"', '')
            consolidated_text = re.sub(r'[0-9.]+', '', consolidated_text)
            
            #Create world cloud graphics for this.
            self.create_word_cloud(
                consolidated_text, 
                "Common processes carried out in 'Stages'", 
                file_path = '/Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/stage_word_cloud_low_level.png')
            
            log.info("Created graphic file in project root directory")
            os.chdir('../..')
            log.info("Change to direcotry %s" %(os.getcwd()))
        except Exception:
            log.info(traceback.format_exc())


if __name__ == '__main__':
    try:
        s = Statistics()
        path = "Repos/jenkins_dataset/"
        s.get_timeout_stats(path)
        s.build_tool_stats(path)
        s.build_word_cloud_high_level(path)
        s.build_word_cloud_low_level(path)
    except Exception:
        log.info(traceback.format_exc())