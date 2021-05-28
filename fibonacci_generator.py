def fibonacci(n) :  
    if(n == 0 or n == 1):
        return n
    elif(n > 1):
        return fibonacci(n-1) + fibonacci(n-2)
          
n = int(input("Enter the no of terms: "))
count = 0
print("The Fibonacci of ", n, "is: ")
for i in range(n+1): 
    print(fibonacci(count))
    count += 1
       
