from StageExtractor import EntityExtractor
from keras.preprocessing.text import text_to_word_sequence
from shlex import shlex
from sklearn.feature_extraction.text import TfidfVectorizer
from cluster import ClusterAnalysis
from sklearn.cluster import KMeans
import pandas as pd
from Statistics import Statistics

import re
import os

class JenkinsClustering:
    '''
    This class is used to cluster the Jenkinsfiles based on the data contained in the build
    stages.
    '''
    def get_data_for_jenkinsfile(self,jenkinsfile):
        try:

            extract = EntityExtractor()
            consolidated_text = ''
            
            elems = list(shlex(open(jenkinsfile)))
            stage_dict = extract.get_all_entities(elems,'stage', None, True)
            data_values = []
            # Get the data in the files contained the build stages
            for key in stage_dict.keys():
                if 'build' in key.lower():
                    data_values.append(stage_dict[key])
            f = list(extract.get_all_entities(elems,'stage', None, True).values())
            if data_values == []:
                return ''
            temp = ' '.join([' '.join(item) for item in data_values])
            file_blob = ' '.join(elems)

            # Consolidate the data inside the build stage as a string 
            consolidated_text += temp
            consolidated_text = text_to_word_sequence(consolidated_text)
            consolidated_text = ' '.join(consolidated_text).replace("'", "").replace('"', '')
            consolidated_text = re.sub(r'[0-9.]+', '', consolidated_text)
            return consolidated_text
        except:
            print(' Unable to get the data for the file: ' + jenkinsfile)
            return ''

    
    def prepare_data_for_clustering(self):
        try:
            # os.chdir('./Jenkinsfiles/')
            jenkinsfiles = os.listdir()

            # Create a dataftame for the data.
            data = []
            df = pd.DataFrame(columns=['file','text', 'labels'])
            files = []

            # Get the data of build stage for each file
            for file in jenkinsfiles:
                text = self.get_data_for_jenkinsfile(file)
                if text != '':
                    data.append(text)
                    files.append(file)
            df['text'] = data
            df['file'] = files
            
            # print(df)
            # print(len(data))
            
            # Create a TF - IDF matrix for the data
            vectorizer = TfidfVectorizer(max_df=1.0, min_df=1,norm = None)
            dataset = vectorizer.fit_transform(df['text'])
            data = dataset.toarray()
            print(data)
            return data, df
        except:
            print('Unable to prepare the data for clustering')
            return None, None



# j = JenkinsClustering()

# data, df = j.prepare_data_for_clustering()
# estimator = KMeans(n_clusters=30, init = 'k-means++', max_iter = 1000)
# estimator.fit(data)
# print(estimator.labels_)

# df['labels'] = estimator.labels_

# for item in set(estimator.labels_):
#     con_string = ''
#     for i in range(len(df)):
#         if df['labels'][i] == item:
#             con_string += df['text'][i]
#     Statistics.create_word_cloud(con_string, "Cluster %s" %(item), '/Users/sandeepjoshi/Documents/CS540/Course_Project/sandeep_joshi__debojit_kaushik_course_project/cluster_%s.png' %(item))
    