"""" 
Homework 4, Exercise 2
Name: Jaden Mascarenhas 
Date: 3/9/23 
Description: Finding phone numbers and email addresses within data using RegEx.
""" 
import re
import pyperclip



#Clipboard data is quantified as a string variable
clipboardData = pyperclip.paste()

#The format to seek phone numbers in RegEx
phoneNumberFormat = re.compile(r'''
    (\()?           #parentheses around the first three since it is an area code(may or may not be used)
    (\d{3})         #First three numbers
    (\))?           #ending the parentheses(may or may not be used)

    (\s|-|\.)?      #hyphen(may or may not be used)

    (\d{3})         #mid three numbers

    (\s|-|\.)       #hyphen

    (\d{4})         #end 4 numbers
''', re.VERBOSE)



#The format to seek email addresses in RegEx
emailAddressFormat = re.compile(r'''
    ([a-zA-Z0-9._%+-]+)             #any amount of these valid characters: lower case & upper case alphanumerics, '.', '_', '%', '+' and '-'
    @                               # the @ symbol marks the end of the username that was listed above
    ([a-zA-Z0-9._]+)                #The first 'level' of the domain name, can include: lower & upper case alphanumerics, '_'
    (\.[a-zA-Z]{2,3})               #The second 'level' of the domain name, can include only '.' followed by 2 or 3 letters(case insensitive)
''', re.VERBOSE)




#initialize the two lists that will hold each of the found type's data
phoneMatches = []
emailMatches = []

#search for phone numbers with the given format by looping through all of the data sequentially
for expr in phoneNumberFormat.findall(clipboardData):
    phNumber = ''
    firstThree = expr[1]
    midThree = expr[4]
    endFour = expr[6]

    #format area codes so that they universally print within parentheses at the beginning
    if firstThree:
        phNumber += '(' + firstThree + ')'

    #concatenate the rest of the 'found' digits with a hyphen seperator into one number
    phNumber += midThree + '-' + endFour

    #add the entire formatted phone number to a list and continue looping 
    phoneMatches.append(phNumber)



#after the above looping has ended, go back to the beginning of the data and search for email adresses with the given format this time
for match in emailAddressFormat.findall(clipboardData):
    emailAddress = match[0] + '@' + match[1] + match[2]
    emailMatches.append(emailAddress)



#Print out phone numbers that were found with the accurate format
if phoneMatches:
    print('Phone numbers found:')
    print('\n'.join(phoneMatches))

#Print out email adresses that were found with the accurate format
if emailMatches:
    print('\nEmail addresses found:')
    print('\n'.join(emailMatches))

