'''
Homework #2, Excercise 3
Name: Jaden Mascarenhas
Date: 2/12/23
Description: This program uses basic funtionality of python to 
             execute a few specified operations upon Lists in python
'''

#This function is used to traverse the list and appropriately place delimiters between list elements
def strList(list):
    #cast list elements to strings(for safety)
    list = str(list)

    #The list is split() and assigned commas between each member except the member -1 (last member), the last member is assigned an 'and' before it 
    csvList=', '.join(list.split(', ')[:-1]) + " and " + list.split(',')[-1]

    #prints the modified list
    print(csvList)


#initialize list to specified elements and print inital elements
stringList = ['Wallet', 'Phone', 'Keys']
print("\n\n")
print(stringList)

#sort elements alphabetically and print
stringList.sort()
print(stringList)

#print only the first term
print(stringList[0])

#print only the specified indexed elements
print(stringList[1:3])

#print only the last element
print(stringList[-1])

#print the index of the specified element
print(stringList.index('Keys'))

#add 'tablet to the list and print modified list
stringList.append('Tablet')
print(stringList)

#add 'mask' as second element on index 1 of the list and print modified list
stringList.insert(1,'Mask')
print(stringList)

#remove the element 'phone' and print modified list
stringList.remove("Phone")
print(stringList)

#reverse the order of the list and print it
stringList.reverse()
print(stringList)

#finally call the function to make the list comma and 'and' seperated.
strList(stringList)


