'''
Homework #2, Excercise 4, Part 1
Name: Jaden Mascarenhas
Date: 2/13/23
Description: This program uses basic funtionality of python to 
             create a number guessing game with a maximum of 10 attempts
'''
#importing the 'random' library, this is required to efficiently randomize the number to guess
import random

#numCalc function's purpose is to decide how the user's input compares to the actual number to be guessed.
#It is both a hint system and a validity check.
def numCalc(numAttempts, input, randomVar):

    if(input>randomVar):
        print("Your guess is too high")

    elif(input<randomVar):
         print("Your guess is too low")

    elif(input==randomVar):
        print("You guessed it correctly in " + str(numAttempts) + " guesses")
        #This function returns true if and only if userInput matches the randomized number. Else, not return anything
        return True

    else:
        print("Invalid input")


#Function that holds most key components, also calls any other necessary functions.
def guessNumber():
    #These variables can be changed to modify the ranges for random number to guess & maximum amount of attempts that the user is allowed.
    minRange=1
    maxRange=20
    maxAttempts=10
    
    #initializers for variables used throughout this function
    userInp=0
    attemptCounter=1
    completeCheck=False

    #defining the randomized number to guess early-on so that it can be used in re-iterating loops
    guessNum=random.randint(minRange,maxRange)


    #This while loop will iterate as long as the current # of guesses is less than the total allowed (in this case 10)
    while(attemptCounter<=maxAttempts):

        #Try-except to catch any invalid userinputs
        try:
            userInp=int(input("Take a Guess:\t"))
        except:
            print("invalid input")
            #balances out the attempt counter at the end so that invalid inputs dont count as guesses
            attemptCounter-=1

        #assigns the return of numCalc() to this variable. Since numCal()c only returns True when there is a 'successful' case, this does not do anything until iteration is supposed to end
        completeCheck=numCalc(attemptCounter, userInp,guessNum)

        #this additional if statement is usually ignored by the code until the 'successful' case (mentioned above) occurs.
        if (completeCheck==True):
            #breaks the while loop early if the user is able to guess under the max amount of guesses
            break

        #this is used to counter the amount of attempts the user has had, increments by 1 everytime there is an attempt
        attemptCounter+=1
    

#Defines the main function which starts the code by calling the guessNumber() function which then calls other necessary functions
def main():
    print("\n\nGuess a number between 1-20, you have 10 tries.")
    guessNumber()

#The code is executed with this last line which calls the main function AFTER all the above functions have been set-up (since this is at the bottom of the code)
main()