'''
Homework #1
Name: Jaden Mascarenhas
Date: 2/2/23
Description: This program uses basic low-level funtionality of python to 
             implement a system that asks security questions to retrieve a passcode.
'''
#SOLUTIONS TO THE CODE: (final code = 'non-existent')
#               Q1: "F" or "f"
#               Q2: "5" 
#               Q3: 3 random, simple multiplication products as the answer (max answer is 45, min answer is 0)
#               Q4: "996"
import random






def securityQuestion1():
    boolVar= input("Q1. Is it false that you desire the code? (T/F): ")


    #Can only have the accepted character 'f' but is case-insensitive and also includes 'F'
    if boolVar.lower() in ['t']:
        return False
    elif boolVar.lower() in ['f']:
        return True
    else:
        return False
    

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'


def securityQuestion2():
    truthVar = "shrek"

    userInp= int(input("Q2. In integers, how many letters are in the title of the greatest animated movie franchise of all time?: "))
    truthVarLength= len(truthVar)              #Key section responsible for the counting of the character legnth


    if truthVarLength==userInp:
        return True
    else:
        return False


'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'


def securityQuestion3():
    print("Q3. Multi-Part Question! You must get at least 2/3 parts correct to proceed: ")
    pointCounter=0


    for x in range(1,4,1):
        num1= random.randint(0,15)              #Key section responsible for the randomizing aspect of Q3.
        num2=x                                  #Although rather obvious, this assigns the iterator 'x' to the variable 'num2'. This will result in the num2 having the same three values in all instances of this code. 
        
        userProduct =int(input("What does the product of " + str(num1) +" * " + str(num2) +" = " ))
        answerProduct=num1*num2
        
        

        #This if-else specifically is a system to count user's points
        if userProduct in [answerProduct]:
            pointCounter+=1
        else:
            continue                            #rather than exiting or returning, continue allows passage through loop without incrementing iterator, effectively creating the 'wrong answer = no points' section of the system
   

    if pointCounter>1:
        print("\nYou got " + str(pointCounter) + " parts correct, you pass this question :)")
        return True
    else:
        print("\nYou only got "+ str(pointCounter) + " parts correct, this question will count as incorrect :(")
        return False

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'


#P(X) is math function to compute under these specified conditions
#       inspired by lecture from Philip Brown in 2023Sp CS 2150 002                                                 
def P(x) :                                      
    mod1 = float(4.5)
    mod2 = float(2)
    return x*x + (mod1%mod2)*x -992514 == 0         #returns a boolean value True or False depending on whether (x) makes the equation equal 0 or not


'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'


def securityQuestion4():
    print("Q4. What is the LARGEST integer in the quantified predicate over the domain D = {-1000, 1000} that makes the following true:")
    largestNum=0
    userInput = int(input("(Existential Quantifier) E is an element on the domain,  x^2 + (1/2)x - " +str(992514) +" = 0:\nx = " )) #Prompts input from user, then immediately casts the received input to type int and assigns to variable for later comparision


    for x in range(1000,-1001,-1):                 #Loops the equation P(x) by plugging-in the descending order of range values and stopping when equation is first satisfied to find the LARGEST integer 
        if P(x):                                   #When the function P(X) returns True, this will assign the iterator outside of the for loop and end the for loop
            largestNum = x
            break


    
    if userInput in [largestNum]:
        return True
    else:
        return False

    
'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'            



def main():
    
    sentinelVal = "non-existent"                                        #This sets a 'sentinel value', this is the correct code. It is a method of input to the system to exit the while loop below and access the 'secret'
    codeInput = input("\nWelcome, I wish you luck in finding my illusive, supposedly non-existent code ;)\n\nEnter the code:")
    validityCheck=None


    #This is a sentinel value loop that cannot be bypassed unless: these questions are successfully completed OR the correct passcode is entered
    while (codeInput != sentinelVal):
        validityCheck=True                                              #Inital setting of True is required to prevent infinite loop of below print() statement in case failure at any point during securityQuestions & to access first question
        print("\nIncorrect response!, you may only acquire the code if you answer ALL of these questions consecutively & correctly: \n")
        


        #A rather large nested-if statements to proceed upon completion of previous condition only
        #Previous conditions are met through the function returning a 'True' boolean value
        if (validityCheck==True):
            print("------------------------------------------------------------------------------------")
            validityCheck=securityQuestion1()
            

            if(validityCheck==True):
                print("------------------------------------------------------------------------------------")
                validityCheck=securityQuestion2()


                if(validityCheck==True):
                    print("------------------------------------------------------------------------------------")
                    print("\n! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")
                    print("\t\tEnough with the boring questions, it is time for some fun with math :)")
                    print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !\n")
                    print("------------------------------------------------------------------------------------")
                    validityCheck=securityQuestion3()  


                    if(validityCheck==True):
                        print("------------------------------------------------------------------------------------")
                        validityCheck=securityQuestion4()


                        if(validityCheck==True):                        
                            print('\t\t\t __________________________')
                            print('\t\t\t| The code is non-existent |')
                            print('\t\t\t ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
                            sentinelVal='non-existent'                  #Internally sets the code to its correct value and thus exits to the secret upon successful completion of questions
                            break


    print("Congratulations! You've won absolutely nothing!!\n")         #This is the final, secret message haha


#Executes the main() (and by extension all other) code (obviously)
main()
