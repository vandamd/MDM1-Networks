# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 07:16:29 2022

@author: lojai
"""

import numpy as np
# Install geneticalgorithm from https://pypi.org/project/geneticalgorithm/
from geneticalgorithm import geneticalgorithm as ga
# Install networkx from https://networkx.org/documentation/stable/install.html
import networkx as nx
import random
import matplotlib.pyplot as plt



class NetworkProblem:
    def __init__(self, N,Min_x,Max_x,Min_y,Max_y):
        self.N = N
        self.Min_x = Min_x
        self.Max_x = Max_x
        self.Min_y = Min_y
        self.Max_y = Max_y
        self.distances = np.zeros((N,N))
        self.cities_dict = {}
        self.solution = []
        self.links = []


    # Calculate the Eucledian distance between two points.
    def eucledian_dis(self,x1,y1,x2,y2):
        return np.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    
    # Cost Function
    def cost_function(self, X):
        
        G = nx.Graph()
        total_length = 0
        penalty = 1
        columns = []
        rows = []
        
        
        # For each gene (bit) that is true in the cromosome (solution) add the distance between the relevant cities 
        for k , connection in enumerate(X):
            if connection:
                # Find the upper triangle matrix cooardinates from the linear cooardinate of the solution.
                # Returns the column and row in the upper traingle matrix of gene based on its order k.
                # https://stackoverflow.com/questions/27086195/linear-index-upper-triangular-matrix
                i = int(self.N - 2 - int(np.sqrt(-8*k + 4*self.N*(self.N-1)-7)/2.0 - 0.5))
                j = int(k + i + 1 - self.N*(self.N-1)/2 + (self.N-i)*((self.N-i)-1)/2)
                
                rows.append(i)
                columns.append(j)
                
                total_length +=  self.distances[i][j]
                
    # Add a penatly for every city that is not    
        for i in range (self.N ):
            if i not in columns and i not in rows:
                penalty += 30
            if i  in columns and i in rows:
               penalty += 50   
    
        for k , item in enumerate(X):
            if item:
    #           https://stackoverflow.com/questions/27086195/linear-index-upper-triangular-matrix
                i = int(self.N - 2 - int(np.sqrt(-8*k + 4*self.N*(self.N-1)-7)/2.0 - 0.5))
                j = int(k + i + 1 - self.N*(self.N-1)/2 + (self.N-i)*((self.N-i)-1)/2)
    
    #           https://networkx.org/documentation/stable/tutorial.html#analyzing-graphs
                G.add_edges_from([(i,j)])
            
    
        if len(list(nx.connected_components(G))) > 1:
            penalty += 1000
            
    
                
            
        return total_length + penalty





    def create_cities_dict_with_random_location(self):
    
        # randomly create N cities with coordinates in the range Min_x,Max_x,Min_y,Max_y
        for i in range(self.N):
            self.cities_dict[i] = (random.randrange(self.Min_x,self.Max_x),random.randrange(self.Min_y,self.Max_y))
            
        return self.cities_dict
                               
    def draw_cities(self):
        # plot the cities.
        for i in self.cities_dict:
            (x, y) = self.cities_dict.get(i)
            plt.scatter(x, y)
            plt.text(x=x, y=y, s=i)
        
        plt.show()
    
    
    
    
    def calc_eucledian_distances_between_cities(self):
        # finding the distances between cities.
        for i, icoordinate in self.cities_dict.items():
            for j, jcoordinate in self.cities_dict.items():
                
                self.distances[i][j] = self.eucledian_dis(*icoordinate,*jcoordinate)
                
                return self.distances
        
    
    
    
    def train_GA(self):
        
        # Genetic algorithm to find best solution to connnect cities.
        
        algorithm_param = {'max_num_iteration': None,\
                           'population_size':100,\
                           'mutation_probability':0.1,\
                           'elit_ratio': 0.01,\
                           'crossover_probability': 0.5,\
                           'parents_portion': 0.3,\
                           'crossover_type':'uniform',\
                           'max_iteration_without_improv':None}
        
        model=ga(function=self.cost_function,dimension=self.N*(self.N-1)/2,variable_type='bool',algorithm_parameters=algorithm_param)
        
        
        
        model.run()
        
        self.solution = model.best_variable
    
        return self.solution

    def draw_cities_and_links(self):
             
        for k , item in enumerate(self.solution):
            if item:
                #  https://stackoverflow.com/questions/27086195/linear-index-upper-triangular-matrix
                i = int(self.N - 2 - int(np.sqrt(-8*k + 4*self.N*(self.N-1)-7)/2.0 - 0.5))
                j = int(k + i + 1 - self.N*(self.N-1)/2 + (self.N-i)*((self.N-i)-1)/2)
        
                
                self.links.append([self.cities_dict[i],self.cities_dict[j]])         
        
        # Plot the cities with thier connected cable
        for i in self.cities_dict:
            (x, y) = self.cities_dict.get(i)
            plt.scatter(x, y)
            plt.text(x=x, y=y, s=i)
        for item in self.links:
            plt.plot([item[0][0],item[1][0]], [item[0][1],item[1][1]])
        
        plt.show()






