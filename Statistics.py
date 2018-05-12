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
import json


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
        self.statistics_dict = {
            'What_are_the_most_used_build_tools?':{},
            'Various_statistics_of_timeouts':{},
            'Do_files_with_parallel_blocks_have_more_stages?':{},
            'What_are_the_most(least)_frequent_post_condition_blocks?':{},
            'Correlation_of_num_triggers_to_avg_num_of_stages':{},
            'Do_different_post_blocks_indicate_more_stages?':{}
        }
        

    def get_post_block_data(self,filepath):
        '''
        For a given jenkinsfile, the method looks for all the blocks used below and gets the number of 
        occurences of them and returns them in a dictionary
        '''
        try:
            extractor = EntityExtractor()
            elements = extractor.get_elements(filepath)
            
            # Extract the content of post block in a jenkinsfile
            post_content = extractor.get_all_entities(elements,'post','post',False)
            post_block_names = ['always','success','failure','unstable','changed','aborted']

            post_elem_dict = []
            for name in post_block_names:
                post_dict = extractor.get_all_entities(post_content,name,name,True)
                post_elem_dict.append(post_dict)
            final_dict = {}

            # Consolidate the data in the dict
            for d in post_elem_dict:
                for key in d.keys():
                    final_dict[key] = d[key]
            return final_dict
            
        except Exception:
            log.info(traceback.format_exc())
            return {}
        
    

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
                    f = open(item)
                    consolidated = reduce(lambda x, y: x+' '+y, list(shlex(f)))
                    f.close()
                    for it in list(build_tools.keys()):
                        #Regex which accepts form of [anything except letters]build_tool_name[space].
                        result = re.findall(r'[^a-zA-Z]+%s\s'%(it), consolidated)
                        if result:
                            build_tools[it] += 1      
                except Exception as e:
                    log.info(e)
                    continue
            verbose_print('Build Tools:')
            self.statistics_dict['What_are_the_most_used_build_tools?'] = build_tools
            print(build_tools)
            
            #Creating a pie chart with the frequncies.
            pie_chart = pygal.Pie()
            pie_chart.title = 'Build tools usage over %s files' %(len(files))
            # For every build tool add frequency to pie chart.
            for item in build_tools:
                pie_chart.add(item, build_tools[item])
            pie_chart.render_to_file("..//build_tools.svg")
            
            #Switch back to root directory to further call methods.
            os.chdir('../')
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
            
            timeout_stats_dict = {}
            self.avg_timeout = sum(self.timeouts)/len(self.timeouts)
            self.timeout_std_dev = statistics.stdev(self.timeouts)
            
            verbose_print("Timeouts:")
            print(self.timeouts)
            timeout_stats_dict['standard_deviation'] = self.timeout_std_dev
            verbose_print("Std Dev of timeouts:") 
            print(self.timeout_std_dev)
            timeout_stats_dict['average_timeout'] = self.avg_timeout
            verbose_print("Avg timeout:")
            print(self.avg_timeout)
            verbose_print("% of files with timeouts: ")
            timeout_stats_dict['percentage_files_with_timeout'] = 100*len(self.timeouts)/len(files)
            print(100*len(self.timeouts)/len(files), '%')

            self.statistics_dict['Various_statistics_of_timeouts'] = timeout_stats_dict

            os.chdir('../')
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
            os.chdir('../')
            self.create_word_cloud(
                consolidated_text, 
                "'Stage' arguments/processes", 
                file_path = './stage_word_cloud.png')
            log.info("Created graphic file in project root directory")

            
            log.info("Change to direcotry %s" %(os.getcwd()))
        except Exception:
            log.info(traceback.format_exc())

    @staticmethod
    def create_word_cloud(text, title ,file_path = None):
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
            # if show:
            #     plt.show()
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
            os.chdir('../')
            #Create world cloud graphics for this.
            self.create_word_cloud(
                consolidated_text, 
                "Common processes carried out in 'Stages'", 
                file_path = './stage_word_cloud_low_level.png')
            
            log.info("Created graphic file in project root directory")
            
            log.info("Change to direcotry %s" %(os.getcwd()))
        except Exception:
            log.info(traceback.format_exc())


    def get_post_block_statistics(self,filepath):
        '''
        This method gets statistics of various post blocks present in a particular Jenkinsfile and
        returns the result as a dictionary with various post blocks as keys and counts as values
        '''
        try:
            elements = list(shlex(open(filepath)))
            log.info('Obtained lexed output for the file: ' + filepath)
            post_block_names = ['always','success','failure','unstable','changed','aborted']

            elem_str = ''
            for elem in elements:
                elem_str = elem_str + elem
            
            result_dict = {}
            has_data = False
            # Loop through all the blocks and get their counts
            for name in post_block_names:
                count = elem_str.count(name)
                result_dict[name] = count
                if count > 0:
                    has_data = True
            if has_data:
                return result_dict
            
            return {}
        except Exception:
            log.info('Unable to obtain shlex output for the file: ' + filepath)
            log.info(traceback.format_exc())
            return {}

    def get_stage_data(self,filepath):
        '''
        Uses the EntityExtractor to extract all the stages present in a jenkinsfile and
        returns the dictionary
        '''
        try:
            extractor = EntityExtractor()
            try:
                elements = extractor.get_elements(filepath)
                log.info('Obtained lexed output for the file: ' + filepath)
            except:
                log.info('Unable to obtain shlex output for the file: ' + filepath)
                return {}

            # Use the entity extractor to get all the elemets inside all the blocks
            stage_data = extractor.get_all_entities(elements,'stage',None,True)
            if stage_data != {}:
                log.info('Obtained stage info for file: ' + filepath)

            return stage_data
        except Exception:
            log.info(traceback.format_exc())
            return {}

    def get_triggers_and_stages(self,filepath):
        '''
            Get triggers and stages for a given file
        '''
        try:
            try:
                f = open(filepath)
                elem = f.readlines()
                f.close()
                log.info('Obtained lexer output for the file: ' + filepath)
            except:
                log.info('Unable to get lexer output for the file: ' + filepath)
                return 0,0
            data_str = ''
            for d in elem:
                data_str = data_str + d
            trigger_count = 0
            num_stages = 0
            # get the number of triggers in the file
            trigger_count = data_str.count('Trigger') + data_str.count('trigger')
            if trigger_count > 0:
                # If the trigger count is >0 only then get the num of stages in the file
                stage_data = self.get_stage_data(filepath)
                num_stages = len(list(stage_data.keys()))
                log.info('Obtained Trigger count: ' + str(trigger_count) + ' Stage Count: ' + str(num_stages) + ' for file: ' + filepath)
            else:
                log.info('Cannot find trigger count for the file: ' + filepath)
            return trigger_count, num_stages
        except Exception:
            log.info(traceback.format_exc())
            return 0,0

    def get_parallel_block_statistics(self):
        '''
            This method gets the average number of stages for files
            1) With parallel blocks
            2) Without parallel blocks
            3) All files
        '''
        try:
            os.chdir('./Jenkinsfiles/')
            filenames = os.listdir('./')
            try:
                filenames.pop(filenames.index('.DS_Store'))
            except:
                pass
            no_stages = 0
            normal_no_stages = 0
            files_without_parallel = 0
            no_stages_for_files_without_parallel = 0
            i = 0
            for jenkinsfile in filenames:
                f = open(jenkinsfile)
                elem = f.readlines()
                f.close()
                text = ''
                # Cumulatively add the number of stages for all the files
                normal_no_stages = normal_no_stages + len(list(self.get_stage_data(jenkinsfile).keys()))
                for t in elem:
                    text = text + t
                cnt = text.count('parallel')
                if cnt > 0:
                    num_stages = len(list(self.get_stage_data(jenkinsfile).keys()))
                    # Cumulatively add the number of stages for the files contianing parallel blocks
                    no_stages = no_stages + num_stages
                    i = i+1
                    log.info(jenkinsfile + 'Count of parallel blocks: ' + str(cnt) + ' Stages: ' + str(num_stages))
                else:
                    # Cumulatively add the number of stages for the files not contianing parallel blocks
                    files_without_parallel += 1
                    no_stages_for_files_without_parallel = no_stages_for_files_without_parallel + len(list(self.get_stage_data(jenkinsfile).keys()))
            
            parallel_block_stats = {}
            parallel_block_stats['average_number_of_stages_per_file_containing_parallel_block'] = float(no_stages)/i
            parallel_block_stats['average_number_of_stages_per_file'] = float(normal_no_stages)/len(filenames)
            parallel_block_stats['average_number_of_stages_per_file_without_parallel_block'] = float(no_stages_for_files_without_parallel)/files_without_parallel

            self.statistics_dict['Do_files_with_parallel_blocks_have_more_stages?'] = parallel_block_stats
            log.info('Average number of Stages per file containing parallel block: ' + str(float(no_stages)/i))
            log.info('Average number of stages per file : ' + str(float(normal_no_stages)/len(filenames)))
            log.info('Average number of stages per file without parallel block: ' + str(float(no_stages_for_files_without_parallel)/files_without_parallel))

            os.chdir('../')
        except Exception:
            log.info(traceback.format_exc())

    def consolidate_post_block_statistics(self):
        '''
            This method calculates the number of occurances of various blocks in the
            post condition blocks of all Jenkinsfiles
        '''
        try:
            os.chdir('./Jenkinsfiles/')
            filenames = os.listdir('./')

            try:
                filenames.pop(filenames.index('.DS_Store'))
            except:
                pass
            post_data = []
            stage_data = []
            post_cond_data = {'always':0,'success':0,'failure':0,'unstable':0,'changed':0,'aborted':0}
            for jenkinsfile in filenames:
                # Get post block statistics for each jenkinsfile and then consolidate to get global statistics
                p_data = self.get_post_block_statistics(jenkinsfile)
                if p_data != {}:
                    post_data.append(p_data)
                    stage_data.append(self.get_stage_data(jenkinsfile))
            names = ['always','success','failure','unstable','changed','aborted']
            # Loop over statistics of each file and then consolidate the data
            for d in post_data:
                for name in names:
                    post_cond_data[name] = post_cond_data[name] + d[name]
    
            pprint.pprint(post_cond_data)
            # Save it for the final results
            self.statistics_dict['What_are_the_most(least)_frequent_post_condition_blocks?'] = post_cond_data
            
            os.chdir('../')
        except Exception:
            log.info(traceback.format_exc())

    def get_trigger_statistics(self):
        '''
            This method is used to see if there is any correlation between number of triggers and number of stages
        '''
        try:
            os.chdir('./Jenkinsfiles/')
            filenames = os.listdir('./')

            try:
                filenames.pop(filenames.index('.DS_Store'))
            except:
                pass
            
            trigger_dict = {}
            for jenkinsfile in filenames:
                # Get number of triggers and stages for each file
                triggers,stages = self.get_triggers_and_stages(jenkinsfile)
                if triggers != 0:
                    # Count them for analysis if a file contains triggers
                    try:
                        trigger_dict[str(triggers)].append(stages)
                    except:
                        trigger_dict[str(triggers)] = [stages]
                    print(jenkinsfile + ' Num Triggers: ' + str(triggers) + ' Num Stages: ' + str(stages))
                else:
                    log.info('No triggers present in the file: ' + jenkinsfile)
                
            print(trigger_dict)
            avg_trigger_dict = {}
            # Loop over the result of each file and consolidate the results
            for key in trigger_dict.keys():
                avg_trigger_dict[key] = float(sum(trigger_dict[key]))/len(trigger_dict[key])
                print(str(key) + ' : ' + str(float(sum(trigger_dict[key]))/len(trigger_dict[key])))

            self.statistics_dict['Correlation_of_num_triggers_to_avg_num_of_stages'] = avg_trigger_dict
            os.chdir('../')
        except Exception:
            log.info(traceback.format_exc())

    def get_post_block_correlation_statistics(self):
        '''
        This method gets the correlation between various post condition blocks and the number of stages
        '''
        try:
            os.chdir('./Jenkinsfiles/')
            filenames = os.listdir('./')

            try:
                filenames.pop(filenames.index('.DS_Store'))
            except:
                pass
            
            # List of the blocks to be analyzed for correlation
            blocks_to_be_analyzed = ['success','always','failure','unstable']
            post_block_corr_dict = {}
            for block in blocks_to_be_analyzed:
                post_data = []
                stage_data = []
                # Loop over all the files for statistics
                for jenkinsfile in filenames:
                    p_data = self.get_post_block_statistics(jenkinsfile)
                    if p_data != {}:
                        post_data.append(p_data)
                        stage_data.append(self.get_stage_data(jenkinsfile))

                    stage_failure_data = {}
                    
                    for i in range(0,len(post_data)):
                        if post_data[i][block] != 0:

                            try:
                                stage_failure_data[str(len(stage_data[i].keys()))].append(post_data[i][block])
                            except:
                                stage_failure_data[str(len(stage_data[i].keys()))] = [post_data[i][block]]
                print('Statistics for the block: ' + block)
                result_dict = {}
                for key in stage_failure_data.keys():
                    result_dict[key] = float(sum(stage_failure_data[key]))/len(stage_failure_data[key])
                    print(str(key) + ' : ' + str(float(sum(stage_failure_data[key]))/len(stage_failure_data[key])))
                post_block_corr_dict[block] = result_dict
            # Saving it in the global dict for json
            self.statistics_dict['Do_different_post_blocks_indicate_more_stages?'] = post_block_corr_dict
            os.chdir('../')
        except Exception:
            log.info(traceback.format_exc())
            


# if __name__ == '__main__':
#     try:
#         s = Statistics()
#         path = "./Jenkinsfiles/"
#         s.get_timeout_stats(path)
#         s.build_tool_stats(path)
#         s.build_word_cloud_high_level(path)
#         s.build_word_cloud_low_level(path)
#         s.get_trigger_statistics()
#         s.consolidate_post_block_statistics()
#         s.get_post_block_correlation_statistics()
#         s.get_parallel_block_statistics()
#         with open('results.json','w',encoding='utf8') as f:
#             f.write(json.dumps(s.statistics_dict, ensure_ascii=False))
        
        
#     except Exception:
#         print(traceback.format_exc())
