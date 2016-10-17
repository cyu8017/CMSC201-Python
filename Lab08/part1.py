'''
Filename: lab8 part1
Author: Zhengchao Yu 
Date: 10/27/2014
Section: 4
E-Mail: zy3@umbc.edu
Description:
Fix code that has syntax errors.
Examples of a syntax error are when you miss a colon,
or forget to close a parenthesis.
'''

# Glance through the code and check to see if anything looks majorily.
# Fix the first error, fix the next error that pops up, etc. 

def findNumInList(num, myList):

    for i in myList:
    
        if i == num:
            print("Found number", num)
          #  return num
        
def main():

    myList = [1, 25, 7, 99, 12]

    # Gets number from user, and appends it to the existing list.
    num = int(input("Enter a number to be added to the end of the list: "))
    myList.append(num)

    # Checks to see if number was successfully added to the list.
    findNumInList(num, myList)
    
main()
