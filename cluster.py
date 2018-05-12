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
import seaborn as sns


class ClusterAnalysis:

    """
        Class for clustering using K-Means Clustering.
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
            log.info("Dataset Missing. Please provide dataset for creating ClusterAnalysis instance.")
        except Exception:
            log.info(traceback.format_exc())

    # Repr class to represented what the class holds.
    def showclass(self):
        try:
            print("Data:", self.data)
            print("No of Clusters:", self.clusters)
            print("Seeds:", self.seeds)
        except Exception:
            log.info(traceback.format_exc())

    #Clustering Using KMeans.
    def performclustering(self):
        try:
            #Initiliase Kmeans form scikit-learn.
            log.info("Clustering initialized.")
            kmeans_model = KMeans(n_clusters = self.clusters, init='k-means++', max_iter = 500).fit(self.data)
            self.model = kmeans_model
            self.labels = kmeans_model.labels_
            self.cluster_centers = kmeans_model.cluster_centers_

            #Assimilate cluster points accoridn tot heir cluster labels.
            for it, item in enumerate(self.labels):
                self.cluster_points[item].append(self.data[it])
            
            log.info("Return data from clustering succesfully.")
            return self.cluster_points, self.cluster_centers
        except Exception:
            log.info(traceback.format_exc())
    

    def predict(self, X):
        try:
            #Predict incoming feature exmamples to their closest cluster.
            return self.model.predict(X)
        except Exception:
            log.info(traceback.format_exc())


#Coloured verbosrity print function for terminal Printing.
def verbose_print(string, color = 32):
    try:
        print("\033[1;%sm%s\033[1;m" %(color, string))
    except Exception:
        log.info(traceback.format_exc())