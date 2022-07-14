#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 03:13:20 2022

@author: sir
"""
import random
import os.path

#checking the existence of a file and remove it
if os.path.exists('myfile.enc'):
  os.remove('myfile.enc')

#Generating the key
alpha='abcdefghijklmnopqrstuvwxyz '
num_alpha=(len(alpha))
main_key=''.join(random.sample(alpha, len(alpha)))
print("Main Key: " +str(main_key))
key=7
with open('code.key', 'w') as file:
    file.write(main_key)

#Enter file e.g message.txt
file=input("Enter the file name: ")
    
# Checking for single extension (.txt) of file

if file.endswith(".txt"):
    try:
        f=open(file,"r")  # reading file
        #Encrypting and reading the file 
        for line in f:
            #Reading the key named alpha
            file=open("code.key","r")
            for alpha in file:
                alpha=alpha.strip()
            #end of key reading
            linestrip=line.strip()
            
            #Encrypting comes here  
            encrypt=''
            for i in linestrip:
                index=alpha.find(i)
                new_index=(index+key)%num_alpha
                encrypt += alpha[new_index]
           
            #Appending lines to the myfile.enc file
            with open("myfile.enc", "a+") as file_object:
                # Move read cursor to the start of file.
                file_object.seek(0)
                # If file is not empty then append '\n'
                data = file_object.read(100)
                if len(data) > 0 :
                    file_object.write("\n")
                    # Append text at the end of file
                file_object.write(encrypt)            
        f.close()

        #Decrypting and reading the file  
        f=open("myfile.enc","r")
        for line in f:
            #Reading the key named alpha
            file=open("code.key","r")
            for alpha in file:
                alpha=alpha.strip()
            #end of key reading
            linestrip=line.strip()
            #Decrypting comes here  
            decrypt=''
            for i in linestrip:
                index=alpha.find(i)
                new_index=(index-key)%num_alpha
                decrypt += alpha[new_index]
            print(decrypt)
        f.close()
        
    except IOError:
        print('There was an error opening the file!')   
  
else:
    print("It must be '.txt' file")
