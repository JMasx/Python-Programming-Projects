"""" 
Homework 3, Exercise 1
Name: Jaden Mascarenhas 
Date: 2/20/23 
Description: Copy a list and re-print it in a different format
""" 


grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']] 

#creates variables for the dimensions of the 2D list (grid)
colsGrid = len(grid)
rowsGrid = len(grid[0])

#fills a new list of transposed dimensions (of original 2D list) with dots
tempGrid=[['.']*colsGrid]*rowsGrid

#iterates through the new list in a transposed way so that values the original 2D list are filled into the new list according to its transposed dimensions
tempGrid = list(map(list, zip(*grid)))      #idea from https://stackoverflow.com/questions/6473679/transpose-list-of-lists

#simply prints the 2D list by rows until it prints all the members it has inside of it, end at " " for new lines
for rows in tempGrid:
    for members in rows:
        print(members, end = " ")
    print()
    