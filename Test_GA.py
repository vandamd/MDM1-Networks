# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 08:03:44 2022

@author: lojai
"""
#!/usr/bin/env python3
import sys
import GA_functions as GA


USAGE_MESSAGE = "Input 5 parameters: number of cities, min x, max x , min y, max y coordinates of the map" 


def print_usage():
    print(USAGE_MESSAGE)
    sys.exit()



def main():
    
   if(len(sys.argv)) != 6:
        print_usage()
        
   # number_of_cities N 
   
   N = int(sys.argv[1])
   Min_x = int(sys.argv[2]) 
   Max_x = int(sys.argv[3])
   Min_y = int(sys.argv[4])
   Max_y = int(sys.argv[5])
   
   
   NP = GA.NetworkProblem(N, Min_x, Max_x, Min_y, Max_y)

   
   NP.create_cities_dict_with_random_location()
   NP.draw_cities()
   NP.calc_eucledian_distances_between_cities()
   solution = NP.train_GA()
   print(solution)
   NP.draw_cities_and_links()
   
   
    
    
    
    

if __name__ == "__main__":
    main()