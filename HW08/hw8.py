'''
   Filename: hw8.py
     Author: Zhengchao Yu 
       Date: 11/7/2014
    Section: 4
     E-Mail: zy3@umbc.edu
Description: HW8
Write a simple 2 player word guessing game. 
The main can be up to 50 line of code (the less the better) 
and needs to have at least 8 functions (more functions could be added). 
Each function should perform a well-defined task. 
'''
# Function: readFile():
# Description:
# This function will prompt the user to enter a text file. 
# If the file is valid, file will open, and program will read file. 
# If the file is not valid, prompt the user to enter another file. 
# Input: text file 
# Output: read file
def readFile():
    
    invalidFile = True 

    # While there is no valid file within the program, 
    # prompt the user to enter a text file. 
    while (invalidFile):
        try: 
            fileName = input("Enter the name of your text file: ")
            
            # If the text file is valid, open and read the file. 
            # If the text file is invalid, prompt for another file. 
            file = open(fileName, "r")
            return file 
        except: 
            print("Enter another file name: ")

# Function: checkInput(): 
# Description: 
# This function will check the users input, 
# by allowing the user to enter a letter.
# Input: letter 
# Output: letterInput
def checkInput():

    invalidInput = True 
    
    # Prompt the user foa letter 
    while(invalidInput):
        letterInput = input("Enter a letter: ")
        
        # After user has entered a letter, 
        # check to see if the letter is valid or invalid.  
        if(len(letterInput) > 1): 
            invalidInput = True
        elif(ord(letterInput) < 65 or ord(letterInput) > 90 and 
             ord(letterInput) < 97 or ord(letterInput) > 123):
            invalidInput = True 
        # If the letter is valid, convert letter to uppercase. 
        else: 
            letterInput = letterInput.upper()
            return letterInput 

# Function: currentInput():
# Description: 
# This function will check the letter that the user has entered. 
# Input: (enteredLetters, enteredChar) 
# Output: True or False 
def currentInput(enteredLetters, enteredChar):
    
    # Check letters that the user has inputted. 
    # If the letter has already been used, print message. 
    # If the letter has not been previously entered, proceed with game. 
    for i in enteredLetters:
        if(i == enteredChar): 
            print("The letter", enteredChar," has already been selected")
            return False 
    return True 

# Function: printWinner():
# Description: 
# This function wiil determine the winner of the game 
# Input: player1, player2
# Output: winner 
def printWinner(player1, player2):
    
    # Determines if player1 wins 
    if(player1 > player2):
        print("Player 1 Wins!")
    
    # Determines if player2 wins 
    elif(player2 > player1):
        print("Player 2 Wins!")

    # Determines if game is draw. 
    else:
        print("The game is a draw")

# Function: closeFile(): 
# Description: 
# This function will close the inputFile. 
# Input: inputFile
# Output: Exit
def closeFile(inputFile):

    # Close file 
    inputFile.close

# Function: printScore():
# Description: 
# This function will display the current score at the end of each round. 
# Input: player1Score, player2Score
# Output: prints scoreboard for both players
def printScore(player1Score, player2Score):
    
    # Prints scoreboard for both players during the game. 
    print("The Score for Player 1 is: " , player1Score,)
    print("The Score for player 2 is: " , player2Score,)
    print("--------------------------------------------")
    print("\n")

# Function: displayTurn():
# Description: 
# This function will display player's turn. 
# Input: player 1 
# Output: turn 
def displayTurn(player1):

    # Player 1's turn 
    if player1: 
        print("Player 1's turn")
        print("-------------------")
    # Player 2's turn 
    if not player1: 
        print ("Player 2's turn")
        print("-------------------")

# Function: displayScoreCount():
# Description: 
# This function will determine the score count for the game. 
# Input: none 
# Output: count
def displayScoreCount():

    count = 0 
    for i in line: 
        if (char == i): 
            count = count + 1
    return count 

# Function: displayCurrentState(): 
# Description: 
# This function will display the current state the game is in. 
# Input: inputtedLetters, line
# Output: string
def displayCurrentState(inputtedletters, line): 
    string = ""
    for char in line: 

        if char in inputtedletters:
            string = string + char
        else:
            string = string + "_"
        string = string + " "
    print(string)

# Function: stringFilled(): 
# Decription: 
# This function will fill the letter within the game. 
# Input: inputtedLetter, line 
# Output: True, False. 
def stringFilled(inputtedLetter, line):

    # If the letter entered is true: 
    # This for loop will fill the blank space with the correct entered letter. 
    for i in line:
        if i not in inputtedLetter:
            return True
    return False 

# Function: guess():
# Description:
# This function checks to see if the guessed letter is correct letter. 
# Input: inputtedLetters
# Output: 
def guess(inputtedLetters, line, letter):

    # If letter exists, return True 
    for i in line: 
        if letter == i: 
            return True 

    # If letter does not exist, print the folllowing error message. 
    print("No letter: ", letter, " in the word")
    return False

# Function: scoreCount(): 
# Description: 
# This function will count the score for both players. 
# Input: line, letter
# Output: score 
def scoreCount(line, letter):

    score = 0
    
    # This for loop will count each player's score. 
    for i in line:
        if letter == i:
            score = score + 1
    return score

# Function: alreadyGuessed():
# Description:
# This function will determine if the input has already been used. 
# Input: inputtedLetters, letter 
# Output: True, False
def alreadyGuessed(inputtedLetters, letter):

    # If the player has entered a letter that has already been guessed, 
    # print [This letter has already been guessed]. 
    if letter in inputtedLetters:
        print("This letter " + letter + " has already been selected")
        return True
    return False

# Function: printResult 
# Description: 
# This function will print the results of the game. 
# If player1 wins, print [Player 1 Wins] 
# If player2 wins, print [Player 2 Wins]
# Input: player1Score, player2Score
# Output: win, draw
def printResult(player1Score, player2Score):
    
    # The following if else statement will print the results of this game.
   
    # If the score of player1 is greater than the score of player2, 
    # the function will print [Player 1 wins]
    if player1Score > player2Score:
        print("Player 1 wins")
    
    # If the score of player1 and player2 are the same, 
    # The function will print [Draw]
    elif player1Score == player2Score:
        print("The game is a draw")

    # If none of the conditions above are satisfied, 
    # the function will print, [Player 2 wins]
    else:
        print("Player 2 wins")

# Function: main():
# Description: 
# The main will run the entire program. 
# Input: none 
# Output: game
def main():

    # Set player1Score, player2Score, and roundNumber = 0 
    player1Score = 0 
    player2Score = 0 
    roundNumber = 0 

    # Read in a file. 
    files = readFile()

    # This for loop will check each line in the file. 
    # If the line contains a set of strings, switch string from lower to upper.
    # Append uppercase letters to inputtedLetters list. 
    for line in files: 
        line = line.upper()
        notFilled = True 
        inputtedLetters = []
        inputtedLetters.append("\n")
        player1 = True 
        roundNumber = roundNumber + 1

        # Print round number for each session of the game. 
        print("Round: ", roundNumber)

        # This while loop will check the player's turn. 
        while(notFilled):
            # Display current state of the game. 
            displayCurrentState(inputtedLetters, line)
            # Determine which player's turn. 
            displayTurn(player1)
            # Print's score for both players. 
            printScore(player1Score, player2Score)
            # Checks and matches input with letters that have been already 
            # guessed, and matches letters with the file for letters that 
            # have yet to be guessed. 
            letter = checkInput()
            alreadyGuesses = alreadyGuessed(inputtedLetters, letter)
            guesses = guess(inputtedLetters, line, letter)

            # If the player enters a letter that has already been guessed, 
            # Subtract a point from their score. 
            if(alreadyGuesses):
                
                if(player1):
                    player1Score = player1Score - 1
                else: 
                    player2Score = player2Score - 1
        
            # If the player enters a letter that is corrent, 
            # and has not been entered yet, append letter to inputtedLetters. 
            elif guesses: 
                if(player1): 
                    player1Score = player1Score + scoreCount(line, letter)
                    inputtedLetters.append(letter)
                else:
                    player2Score = player2Score + scoreCount(line, letter)
                    inputtedLetters.append(letter)

            if(guesses): 
                player1 = not player1
        
            # Display unfilled game field at the beginning of the game. 
            notFilled = stringFilled(inputtedLetters, line)
        # Display the status of the game. 
        displayCurrentState(inputtedLetters, line)
    # Display the current score. 
    printScore(player1Score, player2Score)
    # Display game results. 
    printResult(player1Score, player2Score)
    # Close file.
    closeFile(files)

main()

            
