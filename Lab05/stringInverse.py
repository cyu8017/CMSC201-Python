'''
Filename: stringReverse.py
Author: Zhengnchao Yu 
Date: 10/6/2014
Section: 4
E-Mail: zy3@umbc.edu
Description: Reversing a string!
This program will ask user for a string and then reverse the string and print the output.
This program will not use any other built in functions other than .append()
'''
def main():
    
    # Empty Lists 
    emptyArray = []
    variables = ""

    # Prompt the user to input a string. 
    stringInput = str(input("Enter a string to reverse: "))
    
    # This for loop will identify the range of the input and reverse it. 
    for i in range(len(stringInput)):
        emptyArray.append(stringInput[len(stringInput) -i -1])                     

    # This for loop will combine the list/ 
    for i in emptyArray:
         variables = variables + i 

    # This line will print reverse string. 
    print(variables)

main()
