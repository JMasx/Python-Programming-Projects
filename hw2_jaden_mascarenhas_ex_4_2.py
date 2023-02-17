'''
Homework #2, Excercise 4, Part 2
Name: Jaden Mascarenhas
Date: 2/12/23
Description: This program uses basic funtionality of python to 
             create a number guessing game WITH random upper and lower bounds (max limit of 1000 to save computing resources)
'''


import random




'''                                             numCalc Function                                                           '''
#numCalc function's purpose is to decide how the user's input compares to the actual number to be guessed.
#It is both a hint system and a validity check.
def numCalc(numAttempts, input, randomVar):

    if(input>randomVar):
        print("Your guess is too high\n")

    elif(input<randomVar):
         print("Your guess is too low\n")

    elif(input==randomVar):
        print("You guessed it correctly in " + str(numAttempts) + " guesses")
        #This function returns true if and only if userInput matches the randomized number. Else, not return anything
        return True

    else:
        print("Invalid Input, must be an Natural Number from 1-1000:\n")





'''                                             randomizingNums Function                                                           '''

#Function which calculates both the random bounds and the number to guess between those bounds
def randomizingNums():
    guessNum=0
    limitBound=1000
    lowerBound=0
    upperBound=0

    #randomizes the guessing bounds
    lowerBound= random.randint(1, limitBound)
    upperBound = random.randint(lowerBound, limitBound)
    print("I am thinking of a number between " + str(lowerBound) + " and " + str(upperBound))

    #randomizes the number to guess
    guessNum = random.randint(lowerBound,upperBound)    

    #returns the number to guess 
    return guessNum





'''                                             guessNumber Function                                                           '''
#Function that holds most key components, also calls any other necessary functions.
def guessNumber():
    #Modify to change maximum amount of attempts allowed
    maxAttempts =10

    # Declare + intialize local variables
    userInp=0
    randomNumber=0
    attemptCounter=1
    completeCheck=False
    
    
    randomNumber=randomizingNums()

    #This while loop will iterate as long as the current # of guesses is less than the total allowed (in this case 10)
    while(attemptCounter<=maxAttempts):
        try:
            userInp=int(input("Take a Guess:\t"))
        except:
            print("invalid input")
            #balances out the attempt counter at the end so that invalid inputs dont count as guesses
            attemptCounter-=1

        #assigns the return of numCalc() to this variable. Since numCal()c only returns True when there is a 'successful' case, this does not do anything until iteration is supposed to end
        completeCheck=numCalc(attemptCounter, userInp,randomNumber)


        #this additional if statement is usually ignored by the code until the 'successful' case (mentioned above) occurs.
        if (completeCheck==True):
            #breaks the while loop early if the user is able to guess under the max amount of guesses
            break    


        #this is used to counter the amount of attempts the user has had, increments by 1 everytime there is an attempt
        attemptCounter+=1
    #WHILE loop ends here






'''                                             Main Function                                                           '''    
#Defines the main function which starts the code by calling the guessNumber() function which then calls other necessary functions
def main():
    print("\n\nGuess a number between 1-20, you have 10 tries.")
    guessNumber()


#The code is executed with this last line which calls the main function AFTER all the above functions have been set-up (since this is at the bottom of the code)
main()