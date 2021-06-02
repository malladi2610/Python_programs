"""
Write a program to print a pattern of numbers. The input should be the number of rows.
Example: Input:4

Output:
1
1 2
1 2 3
1 2 3 4
"""

input = int(input("Enter the number to generate the pattern : "))

for i in range(1,input+1):
    for j in range(1,i+1):
        print(j," ",end = "")
    print()