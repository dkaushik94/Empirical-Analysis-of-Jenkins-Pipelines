'''
    Written By Debojit Kaushik (April 2018)
'''
import os
import sys
import traceback
import time
from functools import reduce
from collections import Counter
import json

import pygal
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split 
from sklearn.decomposition import PCA
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from progress.bar import ChargingBar
import seaborn as sns


class ClusterAnalysis:

    """
        Class for clustering using KMeans Clustering.
    """
    def __init__(self, K, dataset = None, seeds = []):
        try:
            assert dataset is not None
            self.clusters = K
            self.seeds = seeds
            self.data = dataset
            self.labels = []
            self.cluster_centers = []
            self.model = None
            self.cluster_points = [[] for i in range(self.clusters)]
        except AssertionError:
            print("Dataset Missing. Please provide dataset for creating ClusterAnalysis instance.")
        except Exception:
            print(traceback.format_exc())

    def showclass(self):
        try:
            print("Data:", self.data)
            print("No of Clusters:", self.clusters)
            print("Seeds:", self.seeds)
        except Exception:
            print(traceback.format_exc())


    def performclustering(self):
        try:
            kmeans_model = KMeans(n_clusters = self.clusters, init='k-means++', max_iter = 500).fit(self.data)
            self.model = kmeans_model
            self.labels = kmeans_model.labels_
            self.cluster_centers = kmeans_model.cluster_centers_
            for it, item in enumerate(self.labels):
                self.cluster_points[item].append(self.data[it])
            
            return self.cluster_points, self.cluster_centers
        except Exception:
            print(traceback.format_exc())
    

    def predict(self, X):
        try:
            return self.model.predict(X)
        except Exception:
            print(traceback.format_exc())



def verbose_print(string, color = 32):
    try:
        print("\033[1;%sm%s\033[1;m" %(color, string))
    except Exception:
        print(traceback.format_exc())
        

# if __name__ == '__main__':
#     try:
#         # print("\033[1;32mSelecting the following features: \033[1;m")
#         verbose_print('\nSelecting the following features:')
#         #Pre-selected features according to choice.
#         features = [
#              'Giving', 
#              'Musical', 
#              'Horror', 
#              'Romantic',  
#              'Gender', 
#              'Compassion to animals', 
#              'Empathy', 
#              'Keeping promises', 
#              'Reading', 
#              'Pets', 
#              'Ageing', 
#              'Daily events', 
#              'Village - town',
#              'Action',
#              'Fake',
#              'Only child'
#             ]
#         verbose_print(features, color = 33)

#         verbose_print("\nCleaning, Preprocessing data, dropping NaN values,converting non-int columns into corresponding values.", color = 36)
#         data = pd.read_csv('responses.csv', encoding = 'utf-8')[features].dropna()
        
#         examples = []
#         #Converting categories into binary values for the two following columns.
#         data['Gender'] = data['Gender'].map({'male': 0, 'female': 1})
#         data['Village - town'] = data['Village - town'].map({'city': 1, 'village': 0})
#         data['Only child'] = data['Only child'].map({'yes': 0, 'no': 1})
        
#         #Creating the feature matrix and converting it to a numpy array.
#         # for item in features:
#         #     examples.append(data[item])
#         # dataset = np.array(examples)
#         # dataset = np.transpose(dataset)


#         verbose_print("Splitting dataset into 80:20 split. (Training:Test)", color = 36)
#         #Train test data split using scikit-learn.
#         data_train, data_test = train_test_split(data, test_size = 0.2) 

#         verbose_print("\nTraining clusters using KMeans")
#         verbose_print('Clusters: 5\nseeds: KMeans++\n', color = 33)
#         c_analyse = ClusterAnalysis(5, data_train.values, seeds = [1,2,3,4,5])
#         cluster_points, cluster_centers = c_analyse.performclustering()


#         #Calculate Averages for each feature.
#         bar = ChargingBar("Evaluating clusters", max = len(cluster_points))
#         averages = []
#         for item in cluster_points:
#             local_avg = [0 for i in range(len(features))]
#             for item2 in item:
#                 for it, item3 in enumerate(item2):
#                     local_avg[it] += item3
#             averages.append([(i / len(item)) for i in local_avg])
#             time.sleep(1)
#             bar.next()
#         bar.finish()

#         # print(averages)

#         cluster_scores = []
#         for item in averages:
#             score = item[0] \
#             + item[1] \
#             - item[2] \
#             + item[3] \
#             + item[4] \
#             + item[5] \
#             + item[6] \
#             + item[7] \
#             + item[8] \
#             + item[9] \
#             + item[10] \
#             + item[11] \
#             + item[12] \
#             - item[13] \
#             - item[14] \
#             + item[15] 
#             cluster_scores.append(score)

#         print('\n', cluster_scores)

#         '''
#             Labels VS Corresponsing Clusters
#                 1: Cluster2,
#                 2: Cluster3,
#                 3: Cluster4,
#                 4: Cluster1,
#                 5: Cluster0
#         '''

#         verbose_print('\nLabels VS Corresponding Clusters')
#         verbose_print('Score 1: Cluster3\nScore 2: Cluster4\nScore 3: Cluster5\nScore 4: Cluster2\nScore 5: Cluster1', color = 36)

#         prediction_labels = c_analyse.predict(data_test)
#         scores = []
#         for item in prediction_labels:
#             if item == 0:
#                 scores.append(5)
#             elif item == 1:
#                 scores.append(4)
#             elif item == 2:
#                 scores.append(1)
#             elif item == 3:
#                 scores.append(2)
#             elif item == 4:
#                 scores.append(3)

                
#         # df = pd.DataFrame(data_train)
#         # df = df.corr()
#         # ax = sns.heatmap(df)
#         # pyplot.show()

        
        
#         verbose_print("\nResults:")
#         verbose_print(scores, color = 37)
#         verbose_print('\nLabels Count')
#         verbose_print(dict(Counter(scores)), color = 37)

#         f = open('Predicted_labels.txt', 'w+')
#         f.write(json.dumps(scores))
#         f.close()
                

#     except Exception:
#         print(traceback.format_exc())