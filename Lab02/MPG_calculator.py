'''
File: MPG_calculator.py
Author: Zhengchao Yu
Date: September 15, 2014
Section: 4
E-Mail: zy3@umbc.edu
Assignment Description: Lab 2: A Simple Program

MPG Calculator
To Calculate a car's MPG you will need two things.

    * Distance the car traveled
    * Amount of gas used
'''

# This line will print program greeting. 
print("This program will calculate MPG")

# Assign two int variables
# Prompt the user to enter the distance tracelled.  
distanceTravelled = int(input("Enter distance travelled: "))
# Prompt user to enter the number of gallons traveled. 
gallonsUsed = int(input("Enter gallons used: "))  

# This line will cast the inputs into a variable. 
MPG = int(((distanceTravelled) / (gallonsUsed))) # This function will calculate MPG

# This line will print MPG calculation. 
print("The MPG is: " + str(MPG))
