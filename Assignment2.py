"""Write a program which takes N as input and generates a 2-dimensional 
array of NxN. The element value in the i-th row will be i.

Ex: 1 1 1
    2 2 2
    3 3 3
    """

N = int(input("Enter the value of N for genrating a n*n matrix: "))
for i in range(1,N+1):
    for j in range(N):
        print(i, end='')
    print()
    
        
        