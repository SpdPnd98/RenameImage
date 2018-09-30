# -*- coding: utf-8 -*-
"""
Spyder Editor

This script file renames all files within a directory according to a specific class name and extension.

Done by SpdPnd98 Bryan Tee Pak Hong
Revised Date: 30 Sept 2018
"""

import os

wd = os.getcwd()
path = input("Enter the path of folder containing all the images: ")
extension = input("Enter the desired extension: ")

print("The directory contains: ")
print(os.listdir(path))

# className = input("Enter class name: ")

i = 1

for file in os.listdir(path):
    # newName = path + "/" + className + str(i) + extension
    newName = path + "/" + str(i) + extension
    curFile = path + "/" + file
    try:
        os.rename(curFile,newName)
    except FileExistsError :
        print("A file of this name already exists!")
        print(newName)
    i += 1


print("Rename Complete! The directory now contains: ")
print(os.listdir(path))
