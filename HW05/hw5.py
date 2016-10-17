'''
Filename: hw5.py
Author: Zhengchao Yu 
Date: 10/10/2014
Section: 4
E-Mail: zy3@umbc.edu
Description:
Create different functions!
Create a single function and it will live in hw5.py
'''

# Function: main():
# Description:
# Tests functions of this program
# Input: None
# Output: Fuunction results 
def main():

    # letterCount(letter, myString) examples
    count1 = letterCount("h", "happy") # Example 1 
    count2 = letterCount("o", "happy") # Example 2 
    count3 = letterCount("p", "happy") # Example 3

    # Prints letterCount examples # 1 - 3 
    print(count1) # Print example 1
    print(count2) # Print example 2
    print(count3) # Print example 3

    # sortList(myList) examples 
    list1 = [4,3,2,6] # first unsorted list
    list2 = [9,60,4,8] # second unsorted list 
    list3 = [21,8,10,9] # third unsorted list
    list1 = sortList(list1) # first sorted list
    list2 = sortList(list2) # second sorted list 
    list3 = sortList(list3) # third sorted list 

    # Prints sortList(myList) examples 1 - 3
    print(list1) # Print example 1
    print(list2) # Print example 2
    print(list3) # Print example 3

    # isPalindrome(myList) examples 1-4
    palindrome1 = isPalindrome("happy")  # example 1
    palindrome2 = isPalindrome("palap")  # example 2
    palindrome3 = isPalindrome("taze")   # example 3
    palindrome4 = isPalindrome("happah") # example 4

    # For the following palindrome examples:
    # If the palindrome is true, print palindrome is true 
    # iF the palindrome is false, print palindrome is false 
   
    # Example 1
    if palindrome1:
        print("palindrome1 True")  
    else:
        print("palindrome1 False")  

    # Example 2
    if palindrome2:
        print("palindrome2 True")  
    else:
        print("palindrome2 False")  

    # Example 3
    if palindrome3:
        print("palindrome3 True") 
    else:
        print("palindrome3 False")

    # Example 4 
    if palindrome4:
        print("palindrome4 True")
    else:
        print("palindrome4 False")
            
# Function: letterCount():
# Description:
# This function takes in a single letter, then a string. 
# Input: letter, myString
# Output: number of occurences 
def letterCount(letter, myString):
    
    count = 0

    # Takes in a letter and then a string. 
    for i in myString:
        if letter == i:
            count += 1

    # Return the number of times letter occurs in myString
    return(count) 

# Function: sortList():
# Description:
# Takes in myList amd return myList sorted. 
# Input: myList 
# Output: myList sorted 
def sortList(myList):

    # This function will take in the length of myList
    for i in range(len(myList)):
        for j in range(len(myList) -1):

            # Rearrange myList in order without using sort(): 
            if myList[j] > myList[j+1]:
               number = myList[j]
               myList[j] = myList[j+1]
               myList[j+1] = number
               
    # Return myList sorted 
    return(myList)

# Function: isPalindrome():
# Description:
# Returns True if myString is a palindrome and False otherwise. 
# Input: myString 
# Output: True, False
def isPalindrome(myString):

    # Returns true if myString is a palindrome
    # (The forward as it is backward).
    for i in range(int(len(myString)/2)):

        # myString will be a single, lowercase word.
        # Returns False if myString is not a palindrome. 
        if myString[i] != myString[len(myString) -i - 1]:
            return False

    return True

main()
