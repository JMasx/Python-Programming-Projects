"""" 
Homework 3, Exercise 4
Name: Jaden Mascarenhas 
Date: 2/20/23 
Description: Program that can play tic-tac-toe using a dictionary
"""
#define the board as a dictionary
boardDict={ 'TL': ' ', 'TM': ' ', 'TR': ' ',
            'ML': ' ', 'MM': ' ', 'MR': ' ',
            'BL': ' ', 'BM': ' ', 'BR': ' '}


def boardPrinter(input):
    #variable initializations
    dimensions=3
    leftWidth=3
    rightWidth=3

    #update the board based on the symbol input sent to this function
    boardDict.update(input)

    #print the entire board in a formatted manner
    print("\n")
    print(boardDict['TL'].center(leftWidth) , '|' , boardDict['TM'].center(leftWidth+rightWidth) , '|' , boardDict['TR'].center(rightWidth),"\n","".center(dimensions*(leftWidth+rightWidth),'_'))
    print(boardDict['ML'].center(leftWidth) , '|' , boardDict['MM'].center(leftWidth+rightWidth) , '|' , boardDict['MR'].center(rightWidth),"\n","".center(dimensions*(leftWidth+rightWidth),'_'))
    print(boardDict['BL'].center(leftWidth) , '|' , boardDict['BM'].center(leftWidth+rightWidth) , '|' , boardDict['BR'].center(rightWidth))
    print("\n")
    




def board():
    #Variable that sets the maximum amount of moves allowed on the board
    maxMoves= 15


    symbolInput=''
    locationInput=''

    #for loop that 'plays turns', loops until the maximum amount of moves is reached
    for i in range(maxMoves):
        try:
            #Stores inputs for row and column coordinates
            rowInput = input("Enter a row to place symbol(T= Top row, M = Middle row, B = Bottom row): ")
            colInput = input("Enter a col to place symbol(L = Left column, M = Middle column, R = Right Column): ")
    
        #catches exceptions thrown by the input() function 
        except:
            print("Invalid location input, exiting program")
            #ends program if there was an exception thrown
            break

        #concatenates and uppercases the coordinate inputs to send to the printing function as a dictionary element
        locationInput =rowInput+colInput
        locationInput = locationInput.upper()

        #Converts input symbol to uppercase to send to printing function
        symbolInput = input("Enter a symbol (X or O): ")
        symbolInput = symbolInput.upper()

        #checks whether the symbol input is valid
        if symbolInput=='X' or symbolInput =='O':
            #creates a variable to store the dictionary pair from input
            newValue={locationInput: symbolInput}
            #sends the pair to the function to print onto the board
            boardPrinter(newValue)

        #prints error and terminates program if invalid symbol was entered
        else:
            print("Invalid Symbol, exiting program")
            break

#runs the board function
board()