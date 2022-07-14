#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 01:46:21 2022

@author: sir
"""
import random
# message=input("enter the message:")
message="hello"
alphabet='abcdefghijklmnopqrstuvwxyz'
key=5
encrypt=''
for i in message:
    index=alphabet.find(i)
    new_index=(index+key)%26
    encrypt += alphabet[new_index]
print(encrypt)
decrypt=''
for i in encrypt:
    index=alphabet.find(i)
    new_index=(index-key)%26
    decrypt += alphabet[new_index]
print(decrypt)


 #Encryption is the process of encoding the data
#i.e converting plain text into ciphertext
#Decryption is doing the reverse

from cryptography.fernet import  Fernet
message ='hello, imapython'
key = Fernet.generate_key()
print(key)


fernet_obj = Fernet(key)

encrypted_message = fernet_obj.encrypt(message.encode())

print(encrypted_message)

with open('test.txt', 'wb') as file:
    file.write(encrypted_message)

decrypted_message = fernet_obj.decrypt(encrypted_message).decode()
print(decrypted_message)

import rsa

message = 'hello, iampython'

publicKey, privateKey = rsa.newkeys(512)


encrypted_message = rsa.encrypt(message.encode(), publicKey)
print(encrypted_message)

decrypted_message = rsa.decrypt(encrypted_message, privateKey).decode()
print(decrypted_message)


message="hello"
alpha='abcdefghijklmnopqrstuvwxyz'

key = ''.join(random.sample(alpha, len(alpha))) 
print(key)

