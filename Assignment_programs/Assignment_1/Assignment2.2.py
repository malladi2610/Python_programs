"""
Write a program to create a matrix of size rxc, provided with the number of rows i.e. r and columns i.e. c as the input. 
The matrix should have elements starting from 1 to rXc with an increment of one in row manner. Example: if r = 2 and c = 3 
then the output is

1 2 3
4 5 6
"""

r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))
count = 0
for i in range(1,r+1):
    for j in range(1,c+1):
        count += 1
        print(count," ",end = "")
    print("")