'''
Name: part3.py
Author: Zhengchao Yu 
Date: 10/1/2014
Section: 4
E-Mail: zy3@umbc.edu
Assignment Description:
Write a program that creates a box made of the * character
The program should ask for the width and height of the box.
(Width first, then height)
The width and height will always be positive.
The inside of the box should not be fill in. 
'''

def main():

    square = 0
    horizontal = 0
    vertical = 0

    # Prompt user to enter length and width of box 
    # Cast input to int
    boxWidth = (int(input("Please enter the width of your box: ")))
    boxHeight = (int(input("Please enter the height of your box: ")))

    # Assign box characters for horizontal and vertical. 
    boxCharacter = '*'
    boxHorizontal = "*"
    boxVertical = "*"
    
    # While loop for box horizontal. 
    while horizontal < (boxWidth-2):
        boxHorizontal = boxHorizontal + boxCharacter
        horizontal += 1

    boxHorizontal = boxHorizontal + "*"

    # While loop for box vertical  
    while vertical < (boxWidth - 2):
        boxVertical = boxVertical + " "
        vertical += 1

    boxVertical = boxVertical + "*"
    print(boxHorizontal)

    vertical = 0

    # While loop for boxHeight
    while vertical < (boxHeight -2):

        vertical += 1
        print(boxVertical)
    # Print square
    print(boxHorizontal)

main()
