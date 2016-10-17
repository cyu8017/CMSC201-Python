'''
Filename: hw7.py
Author: Zhengchao Yu
Date: October 31, 2014
Section: 4
E-Mail: zy3@umbc.edu
Description: 

HW7:
For HW7, Write a filter program that will read the contents of a text file, 
and write out the ASCII values of each alphaNumeric character in a selected 
numeric base. First, prompt the user for a name of a text file (manually 
create the text file before running the program). Prompt the user for a base, 
until you get a valid base (options will be base 2, to base 9).  
'''
# Function: readFile():
# Description: This function will print greeting and view a file. 
# Input: file.txt
# Output: read file 
def viewFile(): # fileView

    # The following line will print program greeting. 
    print("This is a program that will convert your" +
          " text file into ASCII values")
    true = True

    # Prompt the user to input the name of the file. 
    # If the filename is true, read file. 
    while(true):
        try:
            inputFile = input("Enter the name of the file: ")
            print("\n")
            inputFiles = open(inputFile, "r")
            return (inputFiles)
        except:
            a = ""

# Function: writingFile():
# Description: This function will write to file  
# Input: base 
# Output: outputFile
def writingFile(base):
    strings = str(base) + "_myFile.txt"
    outputFile = open(strings, "w")
    return outputFile

# Function: closeFile():
# Description: This function will close the file.  
# Input: inputFile 
# Output: close
def closeFile(inputFile, outputFile):
    outputFile.write("\n")
    inputFile.close()
    outputFile.close()
    
# Function: checkBase
# Description: This function will check the base of the input
# Input: Prompt the user to enter a base 
# Output: number of base
def checkBase():
    flag = True
    number = 0

    while(flag):
        # Prompt the user to enter a base between 2 and 9:
        try:
            base = input("Enter a base between 2 and 9: ")
            number = int(base)

            # The following if statements will check base 
            # If check is true, return number, if false return error. 
            if (number == float(base)
                and number < 10 and number > 1):
                flag = False
            else:
                flag = True

        # If false, return Value error 
        except ValueError:
            a = ""

    # If true, return number 
    return (number)

# Function: remainder():
# Description: This function will find the remainder. 
# Input: numerator, denominator
# Output: remainder
def remainder(numerator, denominator):
    remainders = []
    string = ""

    while numerator != 0:
        remainders.append(numerator % denominator)
        numerator = (numerator / denominator)
        numerator = int(numerator)

    remainders.reverse()

    for i in remainders:
        string = string + str(i)

    string = string + " "
    return string

# Function: convert(): 
# Description: This function will perform conversion. 
# Input: base, inputFile, outputFile
# Output: base conversion 
def convert(base, inputFile, outputFile):
    number = 0

    for line in inputFile:
        for char in line:
            if(number % 5 == 0  and number != 0):
                outputFile.write("\n")
            if(ord(char) < 48 or ord(char) > 58 and
               ord(char) < 65 or ord(char) > 122):
                outputFile.write(".. ")
            else:
                outputFile.write(remainder(ord(char), base))
            number = number + 1

# Function: main()
# Description: Test entire program
# Input: none
# Output: none
def main():

    inputFile = viewFile()
    base = checkBase()
    string = str(base) + "_myFile.txt"
    outputFile = writingFile(base)
    convert(base, inputFile, outputFile)
    closeFile(inputFile, outputFile)
    
    print("Done. Use cat to see the file: " + str(base) 
          + "_" + inputFile.name) 

main()
