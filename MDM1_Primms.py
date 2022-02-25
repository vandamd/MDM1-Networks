import numpy as np
import Generator as G
#import Graph_Generator as Map
import time
start_time = time.time()

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



    
                
def MemberCheck(TestSet, Letters):                      # Takes a list of sets and sees which set a node belongs to
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
             
def ItemSelection(AllPaths,UsablePaths,AddedNode):      # Finds all the new paths for added nodes
    RemovingList = []
    for Path in AllPaths:
        for Node in list(Path[1]):
            if Node == AddedNode:
                UsablePaths.append(Path)
                RemovingList.append(Path)
    for Found in RemovingList:
        AllPaths.remove(Found)            
    return(AllPaths,UsablePaths)

def LetterSelection(item,PreviousNodes):                # Finds out for each append path which new nodes are added
    for Letter in item[1]:
        Counter = 0
        for Node in PreviousNodes: 
            if Letter == Node:
                break
            else:
                Counter += 1
        if Counter == len(PreviousNodes):
            return(Letter)
    return("none")
            
            
def MinimumSpanningTree(AlphOrd,N):                     # Sorted: list of paths, order of mag    
    Divisions = []                                      # Attempt to avoid loops
    CorrectPaths = []                                   # The programs aim
    PathOptions = []
    UsedNodes = ["A"]
    NewNode = "A"
    
    while len(CorrectPaths) < N-1:                      # Stops when the correct number of paths are found
        if NewNode != "none":                           
            AlphOrd,Paths = ItemSelection(AlphOrd,PathOptions,NewNode)
            PathOptions = CombinedListSort(PathOptions)
    
        for item in PathOptions:                          # Loops through every item and also provides their position in the set
            
            Merging = []
            Located = []                                 
            PathLoop = False
            TestLetters = list(item[1])
            
            if len(CorrectPaths)== 0:                       # Auto appends first test
                CorrectPaths.append(item)
                Divisions.append(list(item[1]))
                PathOptions.remove(item)                    # Remove the items from the path options
                NewNode = LetterSelection(item,UsedNodes)
                UsedNodes.extend(list(item[1]))
                UsedNodes = list(set(UsedNodes))
                
                break
            
            for index,subset in enumerate(Divisions):      # Checks if both letters of the name are in the same set 
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
            PathOptions.remove(item)
            NewNode = LetterSelection(item, UsedNodes)
            UsedNodes.extend(list(item[1]))
            UsedNodes = list(set(UsedNodes))
            if len(Located)== 1:
                Divisions[Merging[0]].extend(TestLetters)
                Divisions[Merging[0]]= list(set(Divisions[Merging[0]])) 
                    
            elif len(Located) == 0:
                Divisions.append(TestLetters)
            else:
                Divisions[Merging[0]].extend(Divisions[Merging[1]])
                Divisions.remove(Divisions[Merging[1]])
            break 
    return(CorrectPaths)
            
            
            
def Weights(Input):                                         # Sums the weights of a given list
    Total = 0
    for item in Input: 
        Total += item[0]
    return(Total)
    

# ~~~~~~~~~~~~~~~~~
# ~~ Running Hub ~~
# ~~~~~~~~~~~~~~~~~

def Primms(InputMatrix,N):    
    InputList = MatToUTList(InputMatrix,N)                  # Turns input matrix into an upper triangular list
    Joined = CreateTuple(InputList, N)               # Pairs the upper triangular list with letter pairs
    Sorted = CombinedListSort(Joined)                       # Sorts the combined list
    AllLen = Weights(Sorted)
    Output = MinimumSpanningTree(Joined,N)
    MSTLen = Weights(Output)
    print("Total length of all paths = ",AllLen)
    print("Total Length of MST paths = ",MSTLen)
    print(CombinedListSort(Output))
    print("--- %s seconds ---" % (time.time() - start_time))
    return(Output)


