import numpy as np
import Generator as G
#import Graph_Generator as Map
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

def WierdIdea(Sorted):
    UsedLetters = []                                    # Attempt to avoid loops
    CorrectPaths = []
    Rejects = []
    for index,item in enumerate(Sorted):
        Count = 0                                       # Counts if the point has already been visited
        TestLetters = list(item[1])                     # Turns the two letter path into two list elements
        for letter in UsedLetters:
            if TestLetters[0] ==  letter:               # Checks if letter one is in list
                    Count+=1
            elif TestLetters[1] ==  letter:             # Checks if letter two is in list
                    Count+=1    
            #print(letter,Count)
        if Count == 2:
            Rejects.append(item[1])         # DELETABLE debug check
            continue
        CorrectPaths.append(item)
        UsedLetters.extend(TestLetters)
        UsedLetters = list(set(UsedLetters))
    return(CorrectPaths)

def OccuranceCheck(Subset,MainSet):
    NewVector = []
    Removing = []
    print(Subset,"Space",MainSet)
    
    for index,vector in enumerate(Subset):
        end = False
        while end == False:
            for item in MainSet:
                print(vector,item)
                if vector == item:
                    Removing.append(index)
                    end = True
                    break
            if end == False:
                NewVector.append(vector)
                end = True
    print(Removing)
    return(NewVector,Removing)

def Assembling(Indexs,Startlist,x):
    Extras = []
    #print(Indexs)
    for loop in range(len(Indexs)):
        #print(Indexs)
        Extras.append(Startlist[Indexs[loop]-x])
    return(Extras)
    
                
    


def MinimumSpanningTree(Sorted,N):                        # Sorted: list of paths, order of mag
    # print(Sorted)    
    UsedLetters = []                                    # Attempt to avoid loops
    CorrectPaths = []                                   # The programs aim
    CorrectEven = []
    CorrectOdd = []
    
    EvenElements = []
    OddElements = []
    
    Rejects = []
    for index,item in enumerate(Sorted):                # Loops through every item and also provides their position in the set
        if index%2 == 0:                                # Sorts the items into even or odd by index
            EvenElements.append(item)                   # NOTE: index starts at 0
        else:
            OddElements.append(item)
        #print (item)                                 
        Count = 0                                       # Counts if the point has already been visited
        TestLetters = list(item[1])                     # Turns the two letter path into two list elements
        #print(TestLetters)
        for letter in UsedLetters:
            if TestLetters[0] ==  letter:               # Checks if letter one is in list
                    Count+=1
            elif TestLetters[1] ==  letter:             # Checks if letter two is in list
                    Count+=1    
            #print(letter,Count)
        if Count == 2:
            Rejects.append(item[1])         # DELETABLE debug check
            continue
        CorrectPaths.append(item)                       
        if index % 2 == 0:
            CorrectEven.append(item)
        else:
            CorrectOdd.append(item)
            
        UsedLetters.extend(TestLetters)                 # Adds the new letters to the end of the used list
        UsedLetters = list(set(UsedLetters))            # Takes the set and the list in order to have one occurunce of each letter
    EvenCheck = WierdIdea(EvenElements)                 # Uses the above algorithm on the even and odd elements respectively
    OddCheck = WierdIdea(OddElements)
    Length = len(CorrectPaths)                          # Made into a variable due to recurrance below
    if Length < (N-1):                                  # N-1 is the paths needed for a minimum spanning tree
        E,O = 1,0
        print(CorrectPaths,"\n")
        EvenAdditions = EvenCheck[m.ceil((Length/2)):m.ceil((N-1)/2)]           # Based on total paths = n-1 adds missing letter pairings
        OddAdditions = OddCheck[m.floor((Length/2)):m.floor((N-1)/2)]
        # CorrectPaths.extend(EvenCheck[m.ceil((Length/2)):m.ceil((N-1)/2)])
        # CorrectPaths.extend(OddCheck[m.floor((Length/2)):m.floor((N-1)/2)])
        print("Pre-Occurance",EvenAdditions,OddAdditions)
        if len(OddAdditions) != 0:                                              # Decides which letter pairings are repeated and removes them
            OddAdditions,OIndex = OccuranceCheck(OddAdditions,CorrectPaths)
        if len(EvenAdditions) != 0:
            EvenAdditions,EIndex = OccuranceCheck(EvenAdditions,CorrectPaths)
        try:
            OddAppends = OddAdditions.extend(Assembling(EIndex,OddCheck,O))
        except UnboundLocalError:
            OddAppends = OddAdditions
        try:    
            EvenAppends = EvenAdditions.extend(Assembling(OIndex,EvenCheck,E))
        except UnboundLocalError:
            EvenAppends = EvenAdditions
        try:
            #print(OddAppends)
            CorrectPaths.extend(OddAppends)
        except TypeError:
            print("OddError")
        try: 
            #print(EvenAppends)
            CorrectPaths.extend(EvenAppends)
        except TypeError:
            print("EvenError")
    print(CorrectPaths,UsedLetters,Rejects,"\n",CorrectEven,CorrectOdd)
    print("\n\nEvens:\n", EvenCheck,"\n\nOdds:\n", OddCheck)
    
    return(CorrectPaths)


# def LoopFixing(CorrectPaths): 
#     for Small in CorrectPaths:
#         for Bigger in CorrectPaths[Small:len(CorrectPaths)]:
#             if list(Small)[0] == list(Bigger)[0] or list(Small)[0] == list(Bigger)[1] or list(Small)[1] == list(Bigger)[0] or list(Small)[1] == list(Bigger)[1]:
#                 #Distance = 
#                 #append to matrix
            

# def MinimumSpanningTree(Sorted,N):
#     UsedPairs = []
#     CorrectPaths = []
#     for item in Sorted:
        
        

    
# def Debug(Sorted):
#     prints = 0
#     for item in Sorted:
#         print(item)  
#         prints += 1 
#     print(prints)          
            
        
                    
    
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
#Map.GenerateGraph(MinimumSpanningTree(Sorted,N))
print("\n\n", MinimumSpanningTree(Sorted,N))
#Debug(Sorted)

# ~~~~~~~~~~~~~~~~~~~~~~~
# ~~ Temporary outputs ~~
# ~~~~~~~~~~~~~~~~~~~~~~~

# print(InputMatrix, "\n")
# print(InputList, "\n")
# print(Joined, "\n")
# print (Sorted)
# Map.GenerateGraph()


