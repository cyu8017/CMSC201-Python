'''
   Filename: lab11.py 
     Author: Zhengchao Yu 
       Date: 11/17/2014
    Section: 4
     E-Mail: zy3@umbc.edu
Description: Recursion
For this assignment, you will be doing things that are related. 
The first of which is to write a recursive function that will find the minimum,
element in a list of numbers. 
The second is to create a function that recursively sorts a list of numbers 
from least to greatest using teh findMin function you created. 
'''

# A list sorted from least to greatest has the least element first, 
# and the greatest element last. 
def sort(jumbledList, sortedList):
     newList = []
     jumbledList = [5, 6, 3, 9, 1]
     newList.append(1)
     jumbledList = [5, 6, 3, 9]
     newList.append(3)
     jumbledList = [5, 6, 9]

def findMin(myList, currentMin):
     

     return currentMin
      


def main():
    jumbledList = [404, 398, 119, 147, 243, 367, 44, 291, 328, 309, 79, 498, 
                   310, 436, 321, 41, 354, 30, 281, 239, 65, 207, 186, 308, 
                   72, 406, 458, 418, 442, 271, 448, 262, 407, 18, 149, 196, 
                   210, 326, 247, 414, 129, 496, 264, 280, 453, 387, 15, 4, 
                   273, 452, 173, 317, 27, 212, 121, 27, 121, 366, 169, 85, 
                   297, 235, 224, 460, 187, 120, 319, 362, 396, 390, 408, 464, 
                   213, 208, 204, 303, 66, 215, 277, 13, 206, 200, 165, 110, 
                   211, 378, 112, 278, 112, 6, 337, 133, 97, 353, 52, 295, 
                   124, 471, 274, 455, 141, 231, 413, 47, 440, 7, 67, 329, 
                   249, 441, 145, 237, 336, 130, 117, 43, 108, 444, 457, 360, 
                   183, 17, 154, 46, 38, 251, 90, 283, 349, 179, 316, 36, 
                   466, 69, 238, 463, 246, 394, 76, 276, 426, 456, 40, 358, 
                   216, 202, 499, 75, 483, 214, 487, 470, 222, 417, 312, 50, 
                   252, 100, 480, 427, 490, 194, 102, 305, 21, 339, 106, 131, 
                   205, 105, 340, 467, 282, 155, 451, 391, 402, 3, 377, 122, 
                   430, 126, 176, 351, 74, 217, 338, 476, 80, 376, 445, 128, 
                   137, 352, 115, 150, 55, 123, 219, 81, 381, 492, 482, 261, 
                   478, 384, 420, 132, 343, 114, 241, 432, 244, 403, 473, 475,
                   469, 70, 292, 500, 311, 401, 58, 31, 257, 267, 25, 54, 346, 
                   87, 189, 410, 148, 139, 152, 356, 265, 193, 415, 19, 245, 
                   388, 389, 56, 481, 332, 270, 167, 484, 380, 438, 151, 477, 
                   99, 254, 203, 104, 135, 443, 11, 450, 125, 248, 399, 320, 
                   294, 236, 421, 82, 409, 269, 96, 62, 306, 361, 379, 300, 
                   109, 95, 166, 333, 159, 465, 364, 385, 313, 437, 103 449, 
                   344, 86, 33, 158, 314, 347, 180, 255, 24, 42, 221, 350, 
                   363, 497, 157, 375, 8, 20, 93, 298, 234, 479, 368, 341, 374,
                   331, 230, 172, 60, 428, 424, 201, 286, 279, 296, 73, 439,
                   345, 63, 185, 371, 190, 162, 383]

    min = findMin(jumbledList, jumbledList[0])
    print("The first min is %d" % min)
    jumbledList.remove(min)
    min = findMin(jumbledList, jumbledList[0])
    print("The second min is %d" % min)
    sortedList = sort(jumbledList, [])
    print(sortedList)

main()
