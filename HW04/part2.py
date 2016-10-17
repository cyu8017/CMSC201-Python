'''
Filename: part2.py
Author: Zhengchao Yu
Date: 10/9/2014
Section: 4
E-Mail: zy3@umbc.edu
Description:
Read in a list of numbers entered by the user.
User enter integers and type end to finish.
Print the longest sequence. 
'''
def main():

    longestCount = 0
    currentCount = 0

    # Assign the following variables. 
    currentLetter = ""
    letter = ""

    # While the user does not enter end,
    while letter != "end":
        # Prompt the user to enter a number. 
        letter = input("Enter a number: ")

        # Continue to prompt the user for a number.
        # Stop when user enterd end.
        if letter != currentLetter:
            currentCount = 1
            currentLetter = letter

        # Calculate the longest run within the sequence
        else:
            currentCount = currentCount + 1
            if currentCount >= longestCount:
                longestCount = currentCount

    print("\n")

    # Print the longest count in the sequence. 
    print("Longest run was " + str(longestCount), "long.")

main()
