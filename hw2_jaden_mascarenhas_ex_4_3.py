'''
Homework #2, Excercise 4, Part 3
Name: Jaden Mascarenhas
Date: 2/12/23
Description: This program uses basic funtionality of python to 
             create a number guessing game with:
             Random upper and lower bounds &
             auotmated guesses.

             Bonus: I added a few additional features so that the automated guesses are more accurate.
                    In my testing, the autoGuesser gets the correct number 97% (in 97/100 tests) of the time.
                    In the unlikely event that it is unable to guess, the final guess will usually be within ±0.5% (5 Numbers) away from the actual answer!
'''

import random




'''                                             numCalc Function                                                           '''
#numCalc function's purpose is to decide how the user's input compares to the actual number to be guessed.
#It is both a hint system and a validity check.
def numCalc(numAttempts, input, randomVar):

#Unlike previous excercise parts, this one returns a signal in each control case (except invalid case)
#it helps the autoGuesser decide the bounds and have significantly more accurate guesses
    if(input>randomVar):
        print("Your guess is too high")
        return 1

    elif(input<randomVar):
         print("Your guess is too low")
         return -1
    elif(input==randomVar):
        print("You guessed it correctly in " + str(numAttempts) + " guesses")
        return 0
    else:
        print("Invalid Input, must be an Natural Number from 1-1000:\n")





'''                                             autoGuesser Function                                                           '''
def autoGuesser(prev, bot, top):
    autoGuessNum=0

    #randomizes a number between appropriate ranges as the guess
    autoGuessNum= random.randint(bot, top)


    #Loops if the number calculated above is invalid
    #Valid = not the  same number as the previous guess in this case
    while(prev==autoGuessNum):
        autoGuessNum =  random.randint(bot, top)


    print("Take a guess: " + str(autoGuessNum))

    #returns the verified automatic guess number as the guess.
    return autoGuessNum





'''                                             guessNumber Function                                                           '''
def guessNumber():
    #modify to change code limits
    maxAttempts =10
    limitBound=1000


    # Declare + intialize local variables
    userInp=0
    attemptCounter=1
    completeCheck=0
    lowerBound=0
    upperBound=0
    prevGuess=0

    #randomizing bounds and the number to guess here
    lowerBound= random.randint(1, limitBound)
    upperBound = random.randint(lowerBound, limitBound)
    print("I am thinking of a number between " + str(lowerBound) + " and " + str(upperBound))
    guessNum = random.randint(lowerBound,upperBound)

    #this is an inital bound for the automated guessser, changes over time as guesses are either higher or lower
    botLowerBound = lowerBound
    botUpperBound = upperBound
    



    #While loop to run as long as max attempts are not met
    while(attemptCounter<=maxAttempts):
        try:
            #calls autoGuesser function to assign the automated input to 'userInp'
            userInp=autoGuesser(prevGuess, botLowerBound, botUpperBound)
            
        except:
            print("invalid input")
            #balances out the attempt counter at the end so that invalid inputs dont count as guesses
            attemptCounter-=1


        #assign the current guess as the 'previous guess' AFTER the computations using the guess are complete (calling of autoGuesser() function above achieves this)
        #used for the next iteration of the while loop (if any)
        prevGuess=userInp

        #assigns a signal (-1, 0 or 1) to randomNumber to determine (in)equality comparisions between the autoGuesses and the randomized guessing number    
        completeCheck=numCalc(attemptCounter, userInp,guessNum)

       
    #If-elif-else controls to modify the bounds based on the signal received by 'completeCheck' or begin terminating program   
        if (completeCheck==-1):
            #due to inclusive bounds of the randint() function, add the minimum increment: 1, to the lower bound everytime guess is too low
            botLowerBound=userInp+1

        elif (completeCheck==0):
            #break loop early if successful guess
            break

        elif (completeCheck ==1):
            #due to inclusive bounds in the randint() function, subtract the minimum decrement: 1, to the upper bound everytime guess is too high
            botUpperBound=userInp-1

        #counter for total number of guesses
        attemptCounter+=1


    ###  CAN BE REMOVED BY GRADER  ###  this simply prints the answer after the guessing process is complete
    print("\n\nThe number was " + str(guessNum))
#end of guessNumber Function




'''                                             Main Function                                                           '''
#the definition of the main function that holds the central code to be executed
def main():
    print("\n\nGuess a number between 1-20, you have 10 tries.")
    #call the guessNumber function that executes the rest of the code
    guessNumber()



#call the main function to start executing the code
main()