'''
Homework #2 Ex 2
Name: Jaden Mascarenhas
Date: 2/12/23
Description: This program uses basic low-level funtionality of python to 
             implement a try-except system to catch incorrect type of input value errors
'''

def collatz(number):
    answer=0

    #checks if inputnumber is even (divisible by 2)
    if(number%2==0):
        #divides by two if able to
        answer=((number)//2)
        print(str(answer))
        #returns new value
        return answer

    ##checks if inputnumber is odd (remainder of 1 when divided by 2)
    elif(number%2==1):
        #calculations based on the collatz sequence
        answer=((3*number)+1)
        print(str(answer))
        #returns new value
        return answer

def main():
    #1 is assigned the sentinel exit value, ends code when inputValue = 1
    sentinel=1
   #returnedValue=0
    inputVal=0

    try:
        inputVal=int(input("Enter number: "))
    except:
        #checks invalid inputs
        inputVal=int(input("Must enter integer: "))

        
    while(inputVal != sentinel):   #continues as long as the inputVal doesnt equal 1, the final number
     
        inputVal=collatz(inputVal)


#executes main code
main()