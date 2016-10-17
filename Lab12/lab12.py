'''
   Filename: lab12.py
     Author: Zhengchao Yu 
       Date: 12/1/2014
    Section: 4
     E-Mail: zy3@umbc.edu

Description: Letter Frequencies 
Letter frequencies can be useful for cracking codes in cryptoanalysis or for 
making efficient compression algorithms. In today's lab, you are going to 
compare letter frequencies for the Wikipedia page in French, Spanish, 
Portuguese, Italian, German, and English. 

* Create the program file for this lab. 
* In the file, read each filename from fileslist.txt into a list that you can 
open later. (Remember to use .strip() to get rid of whitespace and newlines). 
* Close fileslist.txt 

* For each filename in your list of filenames: 
* Create an empty dictionary (to hold the characters and their frequency). 
* Use readlines() to read in all the lines from the file into a list. 
* Go through each character in each line: 
* Remove whitespace / newline from beginning and end of line 
* Then for each character in the file, use isalpha() to check if it is 
alphabetic characters only. 
* We only want to ger the frequencies of the alphabetic characters. 
* For the alphabetic characters: 
  * If it is in the dictionaty, increment that character's value 
  * Otherwise, add it to the dictionary with a value of 1
* print a heading indicating which file it is. 
* print the numbers of a's, e's, i's, o's, and u's in the dictionary of 
characters. 
'''
def readFile():
    while True: 
        try:
            filename = input("Enter filename: ")
            files = open(name, "r")
            return files 
        except: 
            a = ""


def closeFile():



def main():

    # For each filename in your list of filenames: 
    # Create an empty dictionary (to hold the characters and their frequency. 
    english = {}
    french = {}
    german = {}
    portuguese = {}
    italian = {}
    spanish = {}
    fileslist = {}

    files = readFile()
    again = True
    
    while again:
        try: 
            



main()
