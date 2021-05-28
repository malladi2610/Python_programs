##Prints whether a given character is in uppercase, lowercase a digit or any other character 

x = input("Enter a Character: ")

if x.isdigit():
    print("The entered character is a number")

elif x.isupper():
    print("The entered character is a Uppercase letter")
    
elif x.islower():
    print("The entered character is a lowercase letter")
    
else:
    print("The entered character is a different character")
    
