'''
Homework #2 ex 1
Name: Jaden Mascarenhas
Date: 2/12/23
Description: This program uses basic low-level funtionality of python to 
             implement the collatz sequence eventually returning in 1.
'''

def collatz(number):
    answer=0
     #checks if inputnumber is even (divisible by 2)
    if(number%2==0):
        answer=((number)//2)
        print(str(answer))
        return answer

##checks if inputnumber is odd (remainder of 1 when divided by 2)
    elif(number%2==1):
        answer=((3*number)+1)
        print(str(answer))
        return answer

def main():
    #1 is assigned the sentinel exit value, ends code when inputValue = 1
    sentinel=1
   #returnedValue=0
    inputVal=0

    inputVal=int(input("Enter number: "))

    while(inputVal != sentinel):
           #continues as long as the inputVal doesnt equal 1, the final number
        inputVal=collatz(inputVal)

main()