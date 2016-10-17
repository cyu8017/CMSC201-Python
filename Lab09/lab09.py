'''
Filename: lab9.py
Author: Zhengchao Yu 
Date: 11/3/2014
Section: 4 
E-Mail: zy3@umbc.edu
Description: 

File I/O

This program will read a list of grades in from a file called grades.txt
and calculating their werighted average a letter grade to it. At the end, 
calculate a class average and write it to the file as well. 

Each line starts with a student name. Afer that, the first value is the weight 
of the grade, followed by the grade itself. This can repeat as many times as 
necessary but the format will 
'''

def getSum(gradesList): 
    sumValue = 0
    grade = ""

    for i in range(1, len(gradesList), 2):
        try:            
            sumValue = sumValue + float(gradesList[i]) * float(gradesList[i + 1])
        except:
            a = ""

    # A 
    if(sumValue > 90.0):
        grade = "A"
    # B 
    elif(sumValue > 80.0):
        grade ="B"
    # C
    elif(sumValue>70.0):
        grade ="C"
    # D
    elif(sumValue>60.0):
        grade="D"
    # F
    else:
        grade="F"

   # print(gradesList[0] + ": " +  str(sumValue) + " - " + grade)
    grade.format(gradesList[0] + ": " + str(sumValue) + " - " + grade)
    
    #openfile.write(gradesList[0] + ": " + str(sumValue) + " - " + grade)
    print(sumValue)
    return sumValue

def main():
    average = 0
    grades = ""
    classAverage = []
    error = False

    openfile = open ("grade_report.txt", "w")
    
    try:
        grades = open("grades.txt", "r")
        
        for i in grades:
            words = i.split()
            number = getSum(words)
            print(number)
            classAverage.append(number)
        
    except:
        error = True
        
    if (error):
        print("File Error")
    
    for i in classAverage:
        average = average + i
        
   # average = (average/ len(classAverage))
   # print("class average is " + str(average))

    grades.close()
    openfile.close()

main()
