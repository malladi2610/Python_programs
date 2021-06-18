"""
Write the program to display the last 10 characters of the string 
“Python Application Programming” on the console.
"""

x = input('Enter a string: ')
n = len(x)
y = x[-1:-10:-1]

print("The last 10 char of the string are : ",y)