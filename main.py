# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 19:36:16 2022

@author: Mahatma
"""

<<<<<<< HEAD:CallingFile.py
import MDM1_Kruskals as Kr
import MDM1_Primms as Pr
=======
from ast import In
import Kruskals as Kr
import Primms as Pr
>>>>>>> fc32722949b685b429c883436200ef36445a607b:main.py
import coordinatesToDistance as Dm
import GraphGen as G
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

"""
The layout of this file is such that....
    ~ for a randomly generated matrix, the size can be chosen  
      with "Matrix Generation Size Input" 
    ~ There are then two running options, the graphing version
      and the testing version. Uncomment the relevant one.
"""


######### Matrix Generation Size Input ##########
N = 24
#################################################


######### Graphing Version ######################
# InputMatrix = Kr.RandMatGen(N)
# print("\nPrimms:")
# G.GenerateGraph(Pr.Primms(InputMatrix,N))
# print("\nKruskals:")
# G.GenerateGraph(Kr.Kruskals(InputMatrix,N))
#################################################


## Testing Version for CASE STUDY ##

# MATRIX INPUT
#InputMatrix = Kr.RandMatGen(N)
InputMatrix = Dm.distanceMatrix

# PRIM'S 
print("\nPrimms:")
#Pr.Primms(InputMatrix,N)
G.GenerateGraph(Pr.Primms(InputMatrix,N), Dm.coordinates)

# KRUSKAL'S
print("\nKruskals:")
#Kr.Kruskals(InputMatrix,N)
G.GenerateGraph(Kr.Kruskals(InputMatrix,N), Dm.coordinates)

# CHECK
X = csr_matrix(InputMatrix)
Tcsr = minimum_spanning_tree(X)
print("\nCorrectness Check\n",Tcsr)
