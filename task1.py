#!python3
'''
Read the data from the file task01.txt
Create a function called find().
Find will require 1 input parameter that is a string literal.
The return value is the line number (starting at 0) that the parameter to be found is on.

Example:
assert find('apple') == 0
assert find('fish') == 5
'''




def find(needle):
    filename = 'task01.txt'
    file = open(filename,"r")
    fileContents = file.read()   
    x = fileContents.split('\n')
    z = 0
    for i in x:
        z += 1
        if i == needle:
         print(z-1)
        

if __name__ == "__main__":
    assert find('apple') == 0
    assert find('fish') == 5