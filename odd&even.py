x = input("Enter the number:")
x = int(x)
if(x > 0):
    
    if x%2 == 0:
        print("Number is Even and positive")
    else:
        print("Number is odd and positive")
        
elif x<0:
    if x%2 == 0:
        print("Number is Even and negative")
    else:
        print("Number is odd and negative")

else:
    print("The number is zero")