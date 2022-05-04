# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 11:28:31 2022

@author: Mahatma
"""

def MatrixPairingList(N):
    List = []
    for First in range(N-1):
        for Second in range(First+1,N):
            List.append(chr(65+First)+chr(65+Second))
    return(List)
