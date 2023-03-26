"""" 
Homework 5, Exercise 1
Name: Jaden Mascarenhas 
Date: 3/24/23 
Description: creates a class that loops through the list starting from the last element and ending on the first element
""" 

## The template for this code was inspired by 'Creating an iter object' from 8_Iterators_and_generators-PR.pdf in Canvas

class ReverseIter:
    def __init__(self, n):
        self.n = n                      #assigns the list that was passed to self.n
        self.i = len(n)                 #assigns the index as the max length of the list, i.e, the last element of the list

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i == 0:                 
            raise StopIteration()         #ends AFTER the index of the current element in the reverse loop is 0,  i.e, the list has ended
        
        self.i -= 1                     #Decrements the index value of the current element the code is looking at to iterate through the list in a reverse order
        return self.n[self.i]           #returns the new index value of the list to repeat the loop


     

it = ReverseIter([1, 2, 3, 4])              #the list given in the assignment example



print(next(it))                             #prints the last element, 4
print(next(it))                             #prints the 2nd last element, 3
print(next(it))                             #prints the element 3rd last element, 2
print(next(it))                             #prints the first element, 1
print(next(it))                             #raises stopIteration error
