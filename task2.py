"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
import math

def pytry(file):

    filename = file
    file1 = open(filename,'r')
    fileContents = file1.read()
    sContents = fileContents.split('\n')
    num = sContents.count('')
    for i in range(num):
        sContents.remove('')
    contents = [sContents[x:x+3] for x in range(0, len(sContents), 3)]
    h = float()
    a = float()
    b = float()
    

    for i in range(len(contents)):
        if contents[i][0] > contents[i][1] and contents[i][0] > contents[i][2]:
            h = float(contents[i][0]) 
            a = float(contents[i][1])
            b = float(contents[i][2])
            if (h**2) == (a**2) + (b**2):
                print(contents[i]) 
            
        else:
            pass        
        if contents[i][1] > contents[i][0] and contents[i][1] > contents[i][2]:
            h = float(contents[i][1])
            a = float(contents[i][0])
            b = float(contents[i][2])
            if (h**2) == (a**2) + (b**2):
                print(contents[i])
            
        else:
            pass
        if contents[i][2] > contents[i][1] and contents[i][2] > contents[i][0]:
            h = float(contents[i][2])
            a = float(contents[i][1])
            b = float(contents[i][0])
            if (h**2) == (a**2) + (b**2):
                print(contents[i])
        else:
            pass

pytry("task02a.txt")
pytry('task02b.txt')