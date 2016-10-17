'''
Name: part4.py
Author: Zhengchao Yu 
Date: 10/1/2014
Section: 4
E-Mail: zy3@umbc.edu
Assignment Description:
Write a program that prints out a triangle made of the * character.
'''
def main():

    triangle = 0

    # Prompt the user to enter the height of the triangle.
    # Cast input to an int
    triangHeight = int(input("Please enter the height of your triangle: "))

    # Assign triangle characer 
    triangleCharacter = '*'
    rightTriangle = ''

    # This while loop will take user input and print triangle
    while triangle < triangHeight:
        rightTriangle = rightTriangle +  triangleCharacter
        print (rightTriangle)
        print()
        triangle = triangle + 1

main()
