
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


class Statistics:

    def __init__(self):
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
        try:
            os.chdir(path)
            files = os.listdir()
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
            for item in list(files):
                try:
                    consolidated = reduce(lambda x, y: x+' '+y, list(shlex(open(item))))
                    for it in list(build_tools.keys()):
                        # print(r'[^a-zA-Z]+%s\s' %(it))
                        result = re.findall(r'[^a-zA-Z]+%s\s'%(it), consolidated)
                        if result:
                            build_tools[it] += 1      
                except Exception:
                    continue
            print('Build Tools:', build_tools)
            pie_chart = pygal.Pie()
            pie_chart.title = 'Build tools usage over %s files' %(len(files))
            for item in build_tools:
                pie_chart.add(item, build_tools[item])
            pie_chart.render_to_file("/Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/build_tools.svg")
            os.chdir('../..')
        except Exception:
            print(traceback.format_exc())
    
    def get_timeout_stats(self, path):
        try:
            os.chdir(path)
            files = os.listdir()

            for item in list(files):
                try:
                    if 'timeout' in list(shlex(open(item))):
                        temp = list(shlex(open(item)))
                        for it in temp[temp.index('timeout'):temp.index('timeout')+5]:
                            if it.isdigit() and float(it) < 1000:
                                self.timeouts.append(float(temp[temp.index(it)]))
                                break
                except Exception:
                    continue

            self.avg_timeout = sum(self.timeouts)/len(self.timeouts)
            self.timeout_std_dev = statistics.stdev(self.timeouts)
            
            print("Timeouts:", self.timeouts)
            print("Std Dev of timeouts:", self.timeout_std_dev)
            print("Avg timeout:", self.avg_timeout)
            print("% of files with timeouts: ", 100*len(self.timeouts)/len(files), '%')

            os.chdir('../..')
        except Exception:
            print(traceback.format_exc())


    def build_word_cloud_high_level(self, path):
        try:
            extractor = EntityExtractor()
            os.chdir(path)
            files = os.listdir()
            consolidated_text = ''
            for item in files:
                try:
                    elems = list(shlex(open(item)))
                    extract_keys = list(extractor.get_all_entities(elems,'stage', None, True).keys())
                    if extract_keys:
                        temp_string = ' '.join([a.lower().strip().replace("'", "").replace('"', '').replace('-', '') for a in extract_keys])
                        consolidated_text += temp_string
                except Exception:
                    continue

            consolidated_text = re.sub(r"[\\]u[0-9]+", "", consolidated_text)
            self.create_word_cloud(
                consolidated_text, 
                "'Stage' arguments/processes", 
                file_path = '/Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/stage_word_cloud.png')
        except Exception:
            print(traceback.format_exc())

    def create_word_cloud(self, text, title ,file_path = None):
        try:
            wc = WordCloud(background_color = "white", height = 400, width = 600,scale = 3, max_words = 1000, margin=10,random_state=1).generate(text)
            default_colors = wc.to_array()
            plt.axis("off")
            if file_path:
                wc.to_file(file_path)
            plt.title(title)
            plt.imshow(default_colors, interpolation="bilinear")
            plt.axis("off")
            plt.show()
        except Exception:
            print(traceback.format_exc())
    
    def build_word_cloud_low_level(self, path):
        try:
            os.chdir(path)
            files = os.listdir()
            consolidated_text = ''
            for item in files:
                try:
                    f = open(item).read()
                    consolidated_text += f
                except Exception:
                    continue
            # print(consolidated_text)
            consolidated_text = text_to_word_sequence(consolidated_text)
            consolidated_text = ' '.join(consolidated_text).replace("'", "").replace('"', '')
            consolidated_text = re.sub(r'[0-9.]+', '', consolidated_text)
            # print(consolidated_text)
            self.create_word_cloud(
                consolidated_text, 
                "Common processes carried out in 'Stages'", 
                file_path = '/Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/stage_word_cloud_low_level.png')
        except Exception:
            print(traceback.format_exc())


if __name__ == '__main__':
    try:
        s = Statistics()
        path = "Repos/jenkins_dataset/"
        # s.get_timeout_stats(path)
        # s.build_tool_stats(path)
        # s.build_word_cloud_high_level(path)
        s.build_word_cloud_low_level(path)
    except Exception:
        print(traceback.format_exc())
