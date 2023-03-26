"""" 
Homework 5, Exercise 2
Name: Jaden Mascarenhas 
Date: 3/24/23 
Description: Finds pythagorean triplets that are exclusively integers
""" 

def take(n, seq):                          #Given by CS3080_Iterators.ipynb as specified by the assignment
                                           #this function will loop and create a list of 'n' amount of elements, 
                                           #It "takes" a certain amount of elements from seq,
                                           #Then converts them into iterators and appends elements into the 'result' list
  seq = iter(seq)
  result = []
  try:
    for i in range(n):
      result.append(next(seq))
  except StopIteration:
    pass
  return result


def pyt(n):
    #Triple for loop to check every combination of x, y and z that are integers until the 'n' value given by the function
    for x in range(1, n+1):
        for y in range(x+1, n+1):
            for z in range(y+1, n+1):


                if x*x + y*y == z*z:       #Given by assigment 
                    yield (x, y, z)        #continually returns the next elements of this function to avoid repetition of returned tuples


def main():
    print(take(10, pyt(50)))                    #Given by assignment

main()