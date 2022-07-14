#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 13:09:22 2022

@author: sir
"""
import numpy as np
from itertools import islice
import pandas as pd
import os.path

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

    def display_file(self):
        try:            
            f=open(self.file,"r")
            return f.read()
            f.close()        
        except IOError:
            return ('There was an error opening the file!')
            

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
            
            
data=Main("data.tx")
print(data.file_check())

line=StudentResults(data)
print(line.read_store_data())
print(line.display_file())
print(line.display_average())