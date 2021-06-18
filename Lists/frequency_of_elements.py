"""
Program to count the frequency of a given element in a list of numbers
"""
list = []
i = 0
count = 0
n = int(input("Enter the number of elements of the list"))

while i < n:
   list.append(int(input("Enter the elements of the list :"))) 
   i += 1
   
x = int(input("Enter the elements to get its frequency : "))
for i in list:
    if(x == i):
        count += 1
print("The frequency of the element ",x, " is ", count)
