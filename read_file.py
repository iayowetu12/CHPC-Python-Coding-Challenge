#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 13:09:22 2022

@author: sir
"""
import sys

import numpy as np
from itertools import islice
import pandas as pd
import os.path
#3. Your main class must create an instance object of the StudentResults class and call all its method.
class Main(str):
    
    def __init__(self, file):
        self.file = file
    
    def file_check(self):
        if self.file.endswith(".txt"):
            return ('"'+self.file + '"' + " to be read!")
        else:
            return ("It must be '.txt' file")

class StudentResults(Main):
    
    def __init__(self, file):
        super().__init__(file)
    
   
    #2.1 A method that reads and stores the data from the text file
    #Data is read and stored in both csv and txt files
    def read_store_data(self):
        try:
            f=open(self.file,"r")
            
            #checking the existence of a file and remove it
            if os.path.exists('temp.txt'):
              os.remove('temp.txt')
              
            idn=[]
            ave=[]
            for line in islice(f,1,None):
                arr=[]
                linestrip=line.strip().split(",")
                for i in range(len(linestrip)-1):
                    if i == 0:    
                        idn.append(linestrip[i])
                        idn_check=linestrip[i]
                    else:
                        arr.append(float(linestrip[i+1]))
                ave.append(np.mean(arr))
                ave_arr=np.mean(arr)
                #Appending lines to the myfile.enc file
                with open("temp.txt", "a+") as file_object:
                    # Move read cursor to the start of file.
                    file_object.seek(0)
                    # If file is not empty then append '\n'
                    data = file_object.read(100)
                    if len(data) > 0 :
                        file_object.write("\n")
                        # Append text at the end of file
                    file_object.write(str(idn_check) + " - " + str(round(ave_arr,1)))  
            f.close()
            
            df = pd.DataFrame(list(zip(idn, ave)),
                            columns =['Std', 'Average'])
            return df
        except IOError:
            return ('There was an error opening the file!')
        
    #2.2 A method that displays the data from the text file
    def display_file(self):
         try:            
             f=open(self.file,"r")
             return f.read()
             f.close()        
         except IOError:
             return ('There was an error opening the file!')
             
    #2.3 A method that works out the average exam score for each student and displays like:   
    def display_average(self):
        try:
            f=open(self.file,"r")
            try:
                f=open("temp.txt","r")
                return f.read()
                f.close()        
            except IOError:
                return ('There was an error opening the file!')
        except IOError:
            return ('There was an error opening the file!')
            


if len(sys.argv) > 1:
    filename = sys.argv[1]
    # print(filename)
    data=Main(filename)
    print(data.file_check())

    line=StudentResults(data)
    print(line.read_store_data()) #code that displays the csv file stored
    print(line.display_file()) #code that displays the original file
    print(line.display_average()) #code tha displays the average
else:
    print('no file received')