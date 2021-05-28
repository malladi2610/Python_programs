"""
Write a program that takes n from the user and calculate sum of following series:

S= (1) + (1+2) + (1+2+3) + ------+ (1+2+3+4+---+n)
"""
n = int(input("Enter the value of n to calculate the sum: "))
sum = 0
for i in range(1,n+1):
    for j in range(0,i):
        sum += i-j
print("The o/p of the series upto",n,"is",sum)