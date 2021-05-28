x = float(input("Enter the first number : "))
y = float(input("Enter the second number : "))
op = input("Enter the operation to be preformed [+ - * / %] : ")
if(op == "+"):
    output = x + y
    print("The addition of ",x ,"and", y ,"is" , output)

elif(op == "-"):
    output = x - y
    print("The substraction of ",x , y ,"is" , output)
    
if(op == "*"):
    output = x * y
    print("The multiplication of ",x , y ,"is" , output)
    
if(op == "/"):
    output = x / y
    print("The division of ",x , y ,"is" , output)
    
if(op == "%"):
    output = x % y
    print("The modulus of ",x , y ,"is" , output)
    
