import math

a = int(input("Enter the first coefficient: "))
b = int(input("Enter the second coefficient: "))
c = int(input("Enter the third coefficient: "))

x = sqrt(round((b*b - 4*a*c),2)

if x == 0:
    print("The roots are real and equal")
    x1 = (-b + x)/2*a
    x2 = (-b - x)/2*a
    print("The roots are: ",x1,x2)

if x > 0:
    print("The roots are real and unequal")
    x1 = (-b + x)/2*a
    x2 = (-b - x)/2*a
    print("The roots are: ",x1,x2)
    
if x < 0:
    print()