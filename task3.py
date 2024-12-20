#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""
import math
## importing file ans splitting one format
subFile= []
fileImport = 'task03.txt'
fileRead = open(fileImport, 'r')
file = fileRead.read()
sFile2 = file.split('\n')
sFile=[]
## convert all elements to int
for i in sFile2:
    if i != "":
        sFile.append(int(i))
    else:
        sFile.append("")

## indexing and splitting file into subfiles on empty elements
lastIndex = -1
for i in range(len(sFile)):
    if sFile[i] == '':
        subFile.append(sFile[lastIndex +1 :  i ])
        lastIndex = i
        
## finding greatest sum and displaying
greatestSum = 0
for i in range(len(subFile)):
    x = sum(subFile[i])
    if x > greatestSum:
        greatestSum = x
print('the greatest sum in this set is >>', greatestSum)

