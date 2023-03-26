"""" 
Homework 5, Exercise 3
Name: Jaden Mascarenhas 
Date: 3/24/23 
Description: Creates modified versions of the range function so that the additional arguments are optional and doesn't use list objects.
""" 


def genrange(stop, start=1, step=1):        #default start index and step values are 1
    temp = start                            #assigns the starting number to temp

    while temp < stop:                      #loops as long as the stop value hasn't been met
        yield temp                          #remembers and returns the start value which is incremented
        temp += step                        #incremented by the amount that is assignemed by the step argument


#Example of only using stop argument
for i in genrange(20):
    print(i)  

print()

#Example of only using stop and start arguments
for i in genrange(20, 0):
    print(i)

print()

#Example of using all the arguments
for i in genrange(20, 0, 5):
    print(i)  
