def factorial(n):
    if(n == 0 or n == 1):
        return(1)
    if(n > 1):
        return(n*factorial(n-1))

num = int(input("Enter the number"))
m = factorial(num)
print(m)