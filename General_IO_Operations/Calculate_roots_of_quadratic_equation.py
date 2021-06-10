import math

a = int(input("Enter the first coefficient: "))
b = int(input("Enter the second coefficient: "))
c = int(input("Enter the third coefficient: "))

dis = b*b - 4*a*c
x = math.sqrt(abs(b*b - 4*a*c))
print(x)

if dis > 0:
    print("The roots are real and unequal")
    x1 = (-b + x)/2*a
    x2 = (-b - x)/2*a
    print("The roots are: ",x1,x2)
    
elif dis==0:
    print("The roots are real and equal")
    x1 = (-b + x)/2*a
    x2 = (-b - x)/2*a
    print("The roots are: ",x1,x2)

else:
    print("The roots are imaginary")
    print(-b/(2*a) , "+j", x)
    print(-b/(2*a) , "-j", x)
    