"""
Homework 6, Exercise 1
Name: Jaden Mascarenhas
Date: 4/4/2023
Description: Adding sleep time gaps using decorators
"""
import functools
import time


#Function template acquired from slowDown.txt provided in class as mentioned in the assignment instructions
def slowDown(rate):     #slowDown argument updated from 'func' to 'rate'
    def decorator(func):
        @functools.wraps(func)
        def wrapperSlowDown(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapperSlowDown
    return decorator


rate= input("Enter a rate(leave blank for default): ")

if rate == '':
    rate=1      #default rate is set to 1 if nothing is entered and an empty string is sent as the input

#string literal with base 10 that was captured as an input is cast into an int    
rate = int(rate)


#slowDown decorator is called with the optional rate argument
@slowDown(rate)
#the countdown decorated function is a recursive function used to test whether the decorator works
def countdown(n):
    if n <= 0:
        print("Finished sleeping")
    else:
        print("Started sleeping")
        countdown(n-1)

#counts down only 1 digit because that is all we need to test whether the sleep funcionality works
countdown(1)

#re-prints the 'rate' variable to illustrate how many seconds the function slept for
print("\nSlept for " + str(rate) + " seconds!")

