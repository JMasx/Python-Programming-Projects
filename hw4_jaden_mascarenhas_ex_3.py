"""" 
Homework 4, Exercise 3
Name: Jaden Mascarenhas 
Date: 3/9/23 
Description: Checks whether a 'password' meets certain requirements using RegEx.
""" 

import re

#manually entered password
password = input("Enter a password: ")

#function that checks whether strength criteria are met
def passwordStrengthChecker(password):

    #(1) Password "is at least eight characters long."
    if re.match(r'^.{8,}$', password):
        print("Passed (1) Length Test")
    else:
        print("Failed (1) Length Test")
        return False
    
    # (2) Password "contains both uppercase and lowercase characters."
    if re.search('[A-Z]', password) and re.search('[a-z]', password):
        print("Passed (2) Case Test")
    else:
        print("Failed (2) Case Test")
        return False
    
    # (3) Password "has at least one digit."
    if re.search('\d', password):
        print("Passed (3) Digit Test")
    else:
        print("Failed (3) Digit Test")
        return False
    

    #Password is strong if it passed all the above criteria
    return True



#Send password received from input to the function
if passwordStrengthChecker(password):
    print("\nThe password is strong!")

else:
    print("\nThe password isn't strong :(")
