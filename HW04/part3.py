'''
Filename: part2.py
Author: Zhengchao Yu
Date: 10/9/2014
Section: 4
E-Mail: zy3@umbc.edu
Description:
Read in a list of two integers.
The user will type end to quit
Print a pairwise sum of these two lists. 
'''

def main():

    # Assign empty lists     
    first = []  # Empty list 1 
    second = [] # Empty list 2 
    third = []  # Pairwise Sum List 

    # Assign variable = 0
    length = 0
    length1 = 0
    i = 0

    # Assign end to quit process 
    end = ""

    # If the user has not entered end, 
    while end != "end":

        # Prompt the user to enter a number and append it to first list. 
        end = input("Enter a number: ")
        length = length + 1
        first.append(end)

    # Assign end to quit process 
    end = ""

    # If the user has not entered end, 
    while end != "end":

        # Prompt the user to enter a number and append it to second list. 
        end = input("Enter a number: ")
        length1 = length1 + 1
        second.append(end)

    if(length > length1):
        i = length1
    else:
        i = length

    # This for loop will calculate pairwise sum after end has been entered.
    for j in range(i):
        if first[j] != "end" and second[j] != "end":
            third.append(int(first[j]) + int(second[j]))

    # Calculate pairwise sum of first list and second list. 
    for j in range((length -i)):
        if first[j + i -1] != "end":
            third.append(int(first[j + i -1]))

    # Calculate pairwise sum list of first list and second list 
    for j in range((length1 -i)):
        if second[j + i - 1] != "end":
            third.append(int(second[j + i -1]))

    # Print pairwise list
    print("\n")
    print(third)
    
main()
