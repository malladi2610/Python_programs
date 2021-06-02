"""
Write a program to input the size of the square matrix and create the matrix with random numbers and convert a square matrix 
into a lower triangular matrix.

Input:
4
12 2 5 6
10 11 4 1
32 1 4 10
1 2 10 9

Output:
12 0 0 0
10 11 0 0
32 1 4 0
1 2 10 9
"""
import random

while True:
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))
    if(r==c):
        rows = r + 1
        col = c + 1
        break
    else:
        print("Please enter same no of rows and columns to generate the square marix")
        continue
  
count = 0
list = [[random.randrange(1,50,1) for i in range(1,rows)] for j in range(1,col)]

for i in range(len(list)):
    for j in range(len(list[i])):
        
        print(list[i][j], end = " ")
    print()
    
print("\nThe Upper triangular matrix of the generated matrix is : \n")
            
for i in range(len(list)):
    for j in range(len(list[i])):
        
        if(i < j):
            list[i][j] = 0
        print(list[i][j], end = " ")
    print()
        
