"""
Homework 6, Exercise 2
Name: Jaden Mascarenhas
Date: 4/10/2023
Description: More efficient runtime in the calculation of the fibonacci sequence using cache

Conclusions: There is a massive difference in efficiency when using @cache and not using it.
We achieved 55 calls with the @cache decorator compared to the 19 calls in the same runtime.
Thus proving that the cache decorator increased efficiency of calculation by 290% !!
"""


import functools
from functools import wraps

#cache decorator is passed a function
def cache(func):
    #function is further passed to wraps
    @wraps(func)

    #funcAttDict acts as a function attribute dictionary to store and check whether a value has already been calculated, so that memory and resources aren't wasted
    def funcAttDict(*args, **kwargs):
        #control to check if the argument provided is already in the dictionary
        if args in funcAttDict.cache:
            return funcAttDict.cache[args]
        #control to add the argument to the dictionary if it was not present within
        else:
            result = func(*args, **kwargs)
            funcAttDict.cache[args] = result
            return result



    funcAttDict.cache = {}
    return funcAttDict



#countCalls function provided in class within the document "9_Decorators-PR.pdf:
def countCalls(func):
    @functools.wraps(func)
    def funcAttDictCountCalls(*args, **kwargs):
        funcAttDictCountCalls.numCalls += 1
        return func(*args, **kwargs)
    funcAttDictCountCalls.numCalls = 0
    return funcAttDictCountCalls



#calls the decorators required for this assignment
@cache
@countCalls
#inefficient version of the fibonnaci function was provided in the assignment itself
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)




#printing the amount of calls achieved by the modified function with cache
print(fibonacci(10))

#printing the amount of calls achieved by the inefficient version of the fibonnaci funtion (Lines 42-45)
print(fibonacci.numCalls)
