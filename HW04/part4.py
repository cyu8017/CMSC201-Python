'''
Filename: part3.py
Author: Zhengchao Yu
Date: 10/3/2014
Section: 4
E-Mail: zy3@umbc.edu
Description:
Start with a variable named myList.
Prompt the user for a single integer, and insert that number into myList.
Keep myList numbers in same order.
print myList
'''

def main():

    # Assign myList numbers
    myList = [1, 9, 16, 24]

    # Prompt the user to tner a number 
    integer = int(input("Enter a number: "))
    inserted = False

    # After the user enters a number,
    # this for loop will calculate rearrange the numbers in order. 
    for i in range(len(myList)):
        if(integer < myList[i] and inserted == False):
            myList.insert(i, integer)
            inserted = True

    if inserted == False:
        myList.append(integer)

    # Print updated myList
    print("\n")
    print(myList)

main()
