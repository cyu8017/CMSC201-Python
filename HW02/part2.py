'''
File: Part2.py
Author: Zhengchao Yu 
Date: September 19, 2014 
Section: 4 
E-Mail: zy3@umbc.edu
Assignment Description: Homework 2
This homework involves a series of exercises designed to practice 
variables, expressions, and if statements. 

Part 2:
For this part, you will create a grade calculator.
Weights will always be between 0 and 1, while the grade will be between 0 and 100.
Once you have computer the weighted sum, print out the letter grade to which that number corresponds. 
'''

import math

def main():

    print("\n")
    # The following line will print this program's greeting. 
    print("WELCOME TO YOUR GRADE CALCULATOR")
    print("--------------------------------------------------------")
    
    # Prompt the user to enter homework weight and homework grade. 
    homeworkWeight = input("Please enter your homework weight between 0 and 1: ")
    homeworkWeight = float(homeworkWeight)
    homeworkGrade = input("Please enter your homework grade: ")
    homeworkGrade = float(homeworkGrade)
    print("--------------------------------------------------------")

    # Prompt the user to enter exam weight and exam grade. 
    examWeight = input("Please enter your exam weight between 0 and 1: ")
    examWeight = float(examWeight)
    examGrade = input("Please enter your exam grade: ")
    examGrade = float(examGrade)
    print("--------------------------------------------------------")

    # Prompt the user to enter discussion weight and discussion grade. 
    discussionWeight = input("Please enter your discussion weight between 0 and 1: ")
    discussionWeight = float(discussionWeight)
    discussionGrade = input("Please enter your discussion grade: ")
    discussionGrade = float(discussionGrade)
    print("--------------------------------------------------------")


    # This equation will calculate the Final Grade 
    FinalGrade = (homeworkWeight * homeworkGrade 
                  + examWeight * examGrade 
                  + discussionWeight * discussionGrade)

    # If FinalGrade is 60, print letter grade F.
    if FinalGrade < 60.0:
        LetterGrade = "F"
    
    # If FinalGrade is 70, print letter grade D.
    elif FinalGrade < 70.0:
        LetterGrade = "D"

    # If FinalGrade is 80, print letter grade C. 
    elif FinalGrade < 80.0:
        LetterGrade = "C"

    # If FinalGrade is 90, print letter grade B. 
    elif FinalGrade < 90.0:
        LetterGrade = "B"

    # If letter grade is above 90, print letter grade A. 
    elif FinalGrade < 100.0: 
        LetterGrade = 'A'

    # This line will print the final letter grade for the course. 
    print("The final grade for this course is: " + str(LetterGrade))    
    print("\n")

main()
