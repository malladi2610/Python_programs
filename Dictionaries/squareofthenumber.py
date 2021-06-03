"""
Write a program which takes n as input and generate a dictionary with elements as the square of the keys
"""
n = int(input("Enter a number :"))

d = {i:i*i for i in range(1,n+1)}

print("The required Dictionary is as follows :")
print(d)