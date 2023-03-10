"""" 
Homework 4, Exercise 1
Name: Jaden Mascarenhas 
Date: 3/9/23 
Description: Calculating shapes' qualities (such as area, perimeter etc.)
""" 
import math

def diagonal(input1, input2):
    diagonalValue=0

    if input2==0:
        diagonalValue = (2* (input1))
        return diagonalValue
    else:
        inp1 = input1 * input1
        inp2 = input2 * input2
        diagonalValue = math.sqrt( ((inp1) + (inp2)) )
        return diagonalValue
        

def area(input1, input2):
    circleArea = 0
    squareArea = 0
    rectangleArea = 0

    if input2==0:
        circleArea = ((math.pi) * (input1 * input1))
        return circleArea
    
    elif input1==input2:
        squareArea = (input1 * input1)
        return squareArea

    elif input1>input2:
        rectangleArea = (input1 * input2)
        return rectangleArea
    


def perimeter(input1, input2):
    circlePeri = 0
    squarePeri = 0
    rectanglePeri = 0

    if input2==0:
        circlePeri = ((math.pi) * (input1 * 2))
        return circlePeri
    
    elif input1==input2:
        squarePeri = (input1 * input1)
        return squarePeri

    elif input1>input2:
        rectanglePeri = (input1 * input2)
        return rectanglePeri



class rectangle:
    length = 20
    width = 10

class circle:
    radius = 0 

class square:
    sideLength = 0



def main():
    circleRadius = (0.5 * diagonal(rectangle.length, rectangle.width))
    circle.radius = circleRadius
    print ("The radius of the circle is " + str(circle.radius))

    circlePerimeter = perimeter(circle.radius,0)
    print ("The circumference of the circle is " + str(circlePerimeter))

main()