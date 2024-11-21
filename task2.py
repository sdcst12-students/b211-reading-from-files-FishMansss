"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
import math
filename = "task02a.txt"
file = open(filename,'r')
filename1 = "task02b.txt"
file1 = open(filename1,'r')

fileContents = file.read()
fileContents1 = file1.read()

cContents = fileContents + fileContents1
sContents = cContents.split('\n')
Contents = sContents.remove("")

print(Contents)

"""
pytry = [] 


for i in sContents:
    if (i**2 + (i+1)**2) == (i+3)**2:
        pytry.append(i)
        pytry.append(i+1)
        pytry.append(i+2)
        
print(pytry)
        
"""