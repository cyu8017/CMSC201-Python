'''
Filename: practice.py
Author: Zhengchao Yu 
Date: 10/20/2014
Section: 4
E-Mail: zy3@umbc.edu
Description:
Lab 07: Practice 
Write a program that takes as an argument a list of integers.
Return a list so that every unique element in the original list.
'''

# Function: groupList(): 
# Description:
# Group list element takes as an list of integers,
# and returns a list that every unique element in 
# the original list is in its own list. 
# Input: list of integers
# Output: grouped list
def groupList(myList):
    
    list1 = []         # Create a new empty list. 
    listIncrement = -1 # Incrementing a list operation to n - 1.
    temp = 0           # Assign tempoary variable equal to 0. 
    
    # This for loop uses bubble sort.
    # Sort numbers in list 1.
    for i in range(len(myList)):
        for j in range(len(myList)):
            if myList[i] < myList[j]:
                number = myList[i]
                myList[i] = myList[j]
                myList[j] = number

    # This for loop will check to see if i is tempoary.
    # If the check is true, then list1 will append the i variable. 
    for i in myList:
        
        if i == temp:
            list1[listIncrement].append(i)

        # If the check is false,
        # Send new number equal to tempoary and compare it to i.
        # If the check is true, append i to list 1. 
        else:

            # Checks to see if tempoary = i. 
            temp = i 
            listIncrement = listIncrement + 1
            list1.append([])
            list1[listIncrement].append(i)

    # Return list1. 
    return list1

# Function: main():
# Description:
# This main function will take in unsorted list 1,
# and return a new sorted list of every element within newList 
# Input: list1
# Output: list2
def main():

    number = '0'

    # Assign values to list1 
    list1 = [1, 2, 3, 1, 1, 2]

    # Create a new list2 
    newList = [[]]

    # Calls groupList function to list2
    list2 = groupList(list1)
    
    print(list2)
   
main()
