# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:04:06 2020

@author: gaby1
"""

import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV, cross_validate
from sklearn.neural_network import MLPClassifier, MLPRegressor  # MLP para classificação
from sklearn import metrics
from sklearn import utils
#from sklearn.externals import joblib
import inspect
import matplotlib.pyplot as plt
import seaborn as sns
import susi




sns.set_style("whitegrid", {'axes.grid': False})

class Data():
    
        
        
    def __init__(self, mlType, filename ,normalizacao, testSize, shuffle=True, output=None):
        
        self.mlType = mlType
        self.filename=filename
        self.output=output
        self.normalizacao= normalizacao
        
        if self.filename.endswith('xlsx'):
                self.dataframe = pd.read_excel(self.filename, index_col=False)
        else:
                self.dataframe = pd.read_csv(self.filename, index_col=False)
        
    
        if output==None:
            self.X= self.dataframe
        else:
            self.X = self.dataframe.drop(self.output, axis = 1)
            self.y = self.dataframe[self.output]
            
       
         
        self.testSize=testSize
        self.shuffle=shuffle

        self.labels = []
        if self.mlType == 1:
            self.labels = self.y.unique()

    def preprocessing(self):
        """
        Normalizes the data with outliers previously removed. Numerical data can be normalized
        using MinMaxScaler, which places all data points between 0 and 1 or StandarScaler, which
        sets data to zero mean and unit variance. Categorical data is encoded for speed.
        """
        if self.mlType == 0: #Clusters
            
            if self.normalizacao == 'Standard':
                Scaler = StandardScaler(copy=True)
                Scaler.fit(self.X)
                self.X = Scaler.transform(self.X)
                return (self.X)
            else:
                MinMax= MinMaxScaler(copy=True)
                MinMax.fit(self.X)
                self.X = MinMax.transform(self.X)
                return (self.X)
                
        else:
            
            if self.normalizacao == 'Standard':
                
                
                X_train, X_test, y_train, y_test = train_test_split(self.X, self.y,
                                                                test_size=self.testSize,
                                                                random_state=None,
                                                                shuffle=self.shuffle)
                self.X_trainScaler = StandardScaler(copy=True)
                self.X_testScaler = StandardScaler(copy=True)
                self.X_trainScaler.fit(X_train)
                self.X_testScaler.fit(X_test)
                X_train = self.X_trainScaler.transform(X_train)
                X_test = self.X_testScaler.transform(X_test)

                return (X_train, X_test, y_train, y_test)
            else:
                X_train, X_test, y_train, y_test = train_test_split(self.X, self.y,
                                                                test_size=self.testSize,
                                                                random_state=None,
                                                                shuffle=self.shuffle)
                self.X_trainMinMax = MinMaxScaler(copy=True)
                self.X_testMinMax = MinMaxScaler(copy=True)
                self.X_trainMinMax.fit(X_train)
                self.X_testMinMax.fit(X_test)
                X_train = self.X_trainMinMax.transform(X_train)
                X_test = self.X_testMinMax.transform(X_test)

                return (X_train, X_test, y_train, y_test)
                

    def getLabels(self):
        return self.labels

class Kohonen_ml:
    def __init__(self,
                 data,# data = (X, y)
                 n_rows= 10,
                 n_columns= 10,
                 #n_iter= 1000,
                 metric= "euclidean",
                 nbh_dist_mode="pseudo-gaussian"):

        self.model = susi.SOMClustering(n_rows=n_rows, n_columns=n_columns,
                                        #n_iter=n_iter,
                                        distance_metric=metric,
                                        nbh_dist_weight_mode=nbh_dist_mode)

        self.X = data

    def train(self):
        self.model.fit(self.X)

    def plot(self,mode=0, alpha=0.2):
        if mode == 0:
            u_matrix = self.model.get_u_matrix()
            plt.imshow(np.squeeze(u_matrix), cmap="jet")
            plt.colorbar()
            #plt.rcParams['figure.figsize'] = (5,6)
            plt.savefig("SOM.png",dpi=75)
            plt.clf()
            
            
        # else:
        #     clusters = self.model.get_clusters(X)
        #     plt.scatter(x=[c[1] for c in clusters], y=[c[0] for c in clusters],
        #                 c=self.y, alpha=alpha)
        #     plt.gca().invert_yaxis()
        #     plt.show()

class RNA_ml:

    def __init__(self,
                 data,# data = (X_train, X_test, y_train, y_test)
                 hidden_layers_sizes=(10,),
                 activation='tanh',
                 solver='lbfgs',
                 alpha=1e-5,
                 max_iter = 1000,
                 tolerance = 1e-3):
        """
        Instanciates a Machine Learning Model with parameters supplied through the interface
        system.
        """
        self.model = MLPClassifier(activation = activation, alpha = alpha,
                                   hidden_layer_sizes = hidden_layers_sizes,
                                   max_iter = max_iter, solver = solver,
                                   tol = tolerance)

        self.X_train, self.X_test, self.y_train, self.y_test = data[0], data[1], data[2], data[3]

    def train(self):
        self.model.fit(self.X_train, self.y_train.ravel())

    def evaluate(self):
        """
        Validades the models with data left out of the training process or test all data avaiable
        in k-fold process (https://machinelearningmastery.com/train-final-machine-learning-model/).
        The score of each split training is printed and result['estimator'] contains a trained model
        for each subset created. The best parameters combination found using GridSearchCV is also printed.
        """
        scores=[]
        self.result = self.model.predict(self.X_test)

        C_dct_metrics = {'F1': metrics.f1_score,
                         'Accuracy': metrics.accuracy_score,
                         'Precision': metrics.precision_score,
                         'Recall': metrics.recall_score}
       
        for key, value in C_dct_metrics.items():
            if 'average' in inspect.getfullargspec(value).args:
                scores.append('{:<15}{:<15.4f}'.format(key, value(self.y_test, self.result, average='weighted')))
            else:
                scores.append('{:<15}{:<15.4f}'.format(key, value(self.y_test, self.result)))
        return scores
        
        

    def plot(self, labels):
        c_matrix = metrics.confusion_matrix(self.y_test, self.result)
        c_matrix = c_matrix.astype('float') / c_matrix.sum(axis = 1)[:, np.newaxis]
        plt.figure(figsize=(5.7, 4.3))  #5.7 , 4
        sns.heatmap(data = c_matrix,
                cmap = 'plasma',
                annot = True,
                xticklabels = labels,
                yticklabels = labels,
                linecolor = 'white',
                linewidths = 1,
                square = True)
        plt.title('Confusion Matrix', fontsize = 12, fontweight = 'bold')
        plt.ylabel('Measured',fontweight= 'bold')
        plt.xlabel('Predicted',fontweight= 'bold')
        plt.tight_layout()
        plt.savefig("ConfusionMatrix.png")
        plt.clf()
        