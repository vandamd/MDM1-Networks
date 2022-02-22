import numpy as np
import Generator as G
import Graph_Generator as Map
import math as m

def RandMatGen (N):
    a = np.random.rand(N, N)                            # set diagonal to 0
    np. fill_diagonal(a, 0)                             # np.tril returns a copy of an array with elements above the k-th diagonal zeroed. 
    M = np.tril(a) + np.tril(a, -1).T                   # lower triangle + a transpose of upper triangle
    return (M)



def MatToUTList(M,N):                                   # Converts the matrix to and upper triangular list
    UTList = []
    X = 0                                               
    while X < N-1:                                      # Loops through Rows until penultimate (last row isnt in upper triangular) 

    # Note loop starts from 0 because matrix row 1 is known as 0 in programming  
    
        for Y in range(X+1,N):                          # Loops through the columns for the upper triangular
            UTList.append(M[X,Y])                       # appends item to the list
        X += 1                                          # selects next row
    return(UTList) 


                                     

def CreateTuple(InputList,N):
    CharacterList = G.MatrixPairingList(N)              # Creates the list of letter pairs
    TupleList = list(zip(InputList,CharacterList))      # Joins Inputs and letter pairs in ordered pairs
    return(TupleList)



def CombinedListSort(ProcessingList):
    ProcessingList.sort(key = lambda x: x[0])           # Sorts the combined list by matrix values
    return(ProcessingList)



    
                
def MemberCheck(TestSet, Letters):
    First  = 0
    Second = 0
    Returns = ""
    if Letters[0] in TestSet:
         First = True
         Returns = Letters[0]
    if Letters[1] in TestSet:
         Second = True
         Returns = Letters[1]
    if First == Second == True:
        return("none")
    return(Returns)
             


def MinimumSpanningTree(Sorted,N):                        # Sorted: list of paths, order of mag    
    Divisions = []                                    # Attempt to avoid loops
    CorrectPaths = []                                   # The programs aim
   
    for item in Sorted:                # Loops through every item and also provides their position in the set
        Merging = []
        Located = []                                 
        PathLoop = False
        TestLetters = list(item[1])                     # Turns the two letter path into two list elements
        if len(Divisions) == 0:                         # The first path becomes a subset
            Divisions.append([TestLetters[0],TestLetters[1]])
            CorrectPaths.append(item)                   # Shortest path is always part of MST
            continue
        for index,subset in enumerate(Divisions):
            FoundLetter = MemberCheck(subset,TestLetters)
            if FoundLetter == "none":
                PathLoop = True
                continue
            if len(FoundLetter) != 0:
                Merging.append(index)
                Located.append(FoundLetter)
        if PathLoop == True:
            continue
        CorrectPaths.append(item)
        if len(Located)== 1:
            Divisions[Merging[0]].extend(TestLetters)
            Divisions[Merging[0]]= list(set(Divisions[Merging[0]]))  
        elif len(Located) == 0:
            Divisions.append(TestLetters)
        else:
            Divisions[Merging[0]].extend(Divisions[Merging[1]])
            Divisions.remove(Divisions[Merging[1]])
    return(CorrectPaths, len(CorrectPaths))
            
            
            
            
            

            
        
                    
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~ Temporary Value Assignment ~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

N = 5                                                # Matrix size (NxN)


# ~~~~~~~~~~~~~~~~~
# ~~ Running Hub ~~
# ~~~~~~~~~~~~~~~~~
#InputList = [,4,67,23,]
InputMatrix = RandMatGen(N)                             # Makes the input matrix
InputList = MatToUTList(InputMatrix,N)                  # Turns input matrix into an upper triangular list
Joined = CreateTuple(InputList, N)                      # Pairs the upper triangular list with letter pairs
Sorted = CombinedListSort(Joined)                       # Sorts the combined list
Map.GenerateGraph(MinimumSpanningTree(Sorted,N))
#print("\n\n", MinimumSpanningTree(Sorted,N))
#Debug(Sorted)

# ~~~~~~~~~~~~~~~~~~~~~~~
# ~~ Temporary outputs ~~
# ~~~~~~~~~~~~~~~~~~~~~~~

# print(InputMatrix, "\n")
# print(InputList, "\n")
# print(Joined, "\n")
# print (Sorted)
# Map.GenerateGraph()


