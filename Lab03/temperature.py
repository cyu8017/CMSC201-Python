'''
Filename: temperatureSuggestions.py
Author: Zhengchao Yu 
Date: 9/22/2014
Section: 4
E-Mail: zy3@umbc.edu
Description:

Lab 3 Simple Logic Conditionals
Temperature Suggestions
'''

def main():

    # Prompt the user to enter a temperature.
    # Cast the input to an int.
    temperatureInput = int(input("Enter temperature: "))

    # Temperature <= 25 condition:
    if temperatureInput <= 25:
        print("Its freezing outside.")

    # Temperature between 25 and 49 condition:
    elif temperatureInput <= 49 and temperatureInput >= 25:
        print("Its a bit chilly, remember to buckle up.")

    # Temperature between 50 and 79 condition: 
    elif temperatureInput <= 79 and temperatureInput >= 50:
        print("The weather is wonderful!")

    # Temperature between 80 and 100 condition: 
    elif temperatureInput <= 100 and temperatureInput >= 80:
        print("It's pretty hot outside!")

    # Temperature above 100 condition: 
    else:
        print("Its way too hot!")

main()
