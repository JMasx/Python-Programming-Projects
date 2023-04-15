"""
Homework 6, Exercise 3
Name: Jaden Mascarenhas
Date: 4/14/2023
Description: Building a custom multi-text clipboard.
"""
import pyperclip
import sys


#writes the clipboard data inside the file 
def writeFile(inputData):
    with open('tempClipboard.txt', 'w') as file:                   #opens a file with this name, creates if non-existent
        for keyWord, data in inputData.items():                    #loops while there are items of data within 'inputData'
            file.write(keyWord + '\t' + data + '\n')               #writes data in a general ordered pair-like format with a delimiter of ' '


#reads the file for dictionary data
def readFile():
    with open('tempClipboard.txt') as file:                         #opens an already existing file with the default 'read only' option
        dictValue = dict(line.strip().split('\t') for line in file) #strips the data inside the file into a dictionary of keyword and paired data for ease-of-access
        return dictValue                                            #returns this afforementioned dictionary





#when there are only two arguments (including 'mcb.py')
if len(sys.argv) == 2:

    #case 1: a keyword is called, check all keywords to see whether the entered one is within the list
    if sys.argv[1] in readFile():         #2nd argument must be the keyword by itself
        tmp = readFile()
        pyperclip.copy(tmp[sys.argv[1]])
        print(tmp[sys.argv[1]])             #print out the associated pair of data inside the dictionary with the inputted keyword



    #case 2: list of keywords is read from the file using the readFile function and the keys() method of dictionaries
    elif sys.argv[1] == 'list':               #2nd argument must be 'list'
        print(list(readFile().keys()))

    
        

#when there are three arguments
elif len(sys.argv) == 3:

    if sys.argv[1] == 'save':               #3rd argument must be 'save'
        tmp = readFile()
        tmp[sys.argv[2]] = pyperclip.paste()    #outputs the clipboard data with the given keyword in the 3rd argument as a dictionary pair onto the file
        writeFile(tmp)                             #uses the writeFile function to write the data onto the file






