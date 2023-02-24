"""" 
Homework 3, Exercise 2
Name: Jaden Mascarenhas 
Date: 2/20/23 
Description: Take a string as an input and count the characters in it
""" 
import pprint

#assign the test string here
strValue="The quick brown fox jumps over the lazy dog"

#initialize variables to be used 
strDictionary = { }
tempChar=''
tempCount =0

#loop until every character in the string has been checked
for i in range(len(strValue)):
    #assign a variable to hold the current character that is being checked
    tempChar= strValue[i]
    #reset the count to 0 for every NEW character
    tempCount=0

    #additional for loop to check for matches of the current character in the entire string
    for j in range (len(strValue)):
        if(strValue[j]==tempChar):
            #increment counter if a match was found
            tempCount+=1
    #at the end of the second for loop, send the checked character along with the amount of occurences to a dictionary outside of the loops         
    strDictionary [tempChar] = tempCount    

#at the end of both loops, print the entire dictionary which shows total occurences for each character.
pprint.pprint(strDictionary)