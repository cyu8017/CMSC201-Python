'''
Filename: part1.py
Author: Zhengchao Yu 
Date: 10/9/2014
Section: 4
E-Mail: zy3@umbc.edu
Description: 
This program will take two numbers as input. 
[A Width & A Height]
Create a square where there are width numbers on each line. 

'''

def main():
    
    # Take in two numbers a an input.
    width = input("Input a width: ") # Prompt for width 
    height = input("Input a height: ") # Prompt for height

    # Assign width and height to start at 0. 
    heightCounter = 1
    widthCounter = 1
    
    # Assign Variable 
    string = ""

    # This for loop will calculate the area of the box. 
    # Multiply width by height
    for i in range( (int(width) * (int(height))) ):
        string = string + " " + str(i)
        widthCounter = widthCounter + 1
        
        if(widthCounter % int(width) == 0):
            # Print box
            print(string)
            string = ""
            widthCounter = 0

main()
