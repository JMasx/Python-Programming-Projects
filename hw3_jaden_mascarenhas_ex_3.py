"""" 
Homework 3, Exercise 3
Name: Jaden Mascarenhas 
Date: 2/20/23 
Description: Add, Delete & Display the items from a dictionary.
""" 

#Defintion of the given initial dictionary
inventory = {
"Hand sanitizer": 10, 
"Soap": 6, 
"Kleenex": 22, 
"Lotion": 16, 
"Razors": 12 
}



def printInventory(inventory):
#Column justification formats of printInventory() was inspired by printPicnic() function given in class
    #sets values for left and right margin widths of the printed table
    leftWidth=15
    rightWidth=5

    #prints a Title header that is centered based on teh margin widths of the table
    print("\n","Inventory".center(leftWidth + rightWidth, '-'),"\n")

    #Loops until each element(item) of dict has been printed on a new line
    for k, v in inventory.items():
        print(k.ljust(leftWidth, '-') + str(v).rjust(rightWidth))

    #extra space at the completion of this function for pretty formatting purposes
    print()



def addItem(inventory, item):
    newValue=''

    #retrieve the amount of the specified item, increment it by 1
    try:
        valueCount = inventory.pop(item)
        valueCount += 1
    
    #exception occurs if the item isnt in the dictionary (count = 0), in this case, set the count to 1
    except:
        valueCount=1

    #assign the new updated dictionary pair to a variable and update it in the original dictionary
    newValue={item: valueCount}
    inventory.update(newValue)



def deleteItem(inventory, item):
    newValue=''
    #retrieve the amount of the specified item, increment it by 1
    try:
        valueCount = inventory.pop(item)
        valueCount -= 1

    #exception occurs if the item isnt in the dictionary (count = 0), in this case, print error message
    except:
        print("\n",item ,"cannot be deleted any further, it does not exist in the inventory")



    #assign the new updated dictionary pair to a variable and update it in the original dictionary
    try:
        newValue={item: valueCount}
        inventory.update(newValue)

    #Used to supress the error that would occur if you tried to delete an item that was never added to the list
    except:
        print()



#Change as needed for testing
def main():
    printInventory(inventory)

    addItem(inventory, 'Advil')
    printInventory(inventory)

    deleteItem(inventory, 'Advil')
    printInventory(inventory)


main()