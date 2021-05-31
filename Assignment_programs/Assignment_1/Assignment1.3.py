"""
Write a program which takes N as input and print the series from 1 till N. 
It also prints BIZZ if a number is divisible by 3, BUZZ if divisible by 
5 and BIZZBUZZ if divisible by both 3 and 5.
"""

def bizzbuzz(N):
    for i in range(1,n+1):
        if(i% 15 == 0):
            # if(i % 5 == 0){
            print(i, "-", "BIZZBUZZ")      
     
        elif(i % 3 == 0):
            print(i, "-", "BIZZ") 
     
        elif(i % 5 == 0):
            print(i, "-", "BUZZ")
          
        else:
            print(i)    
     
n = int(input("Enter the no. of values to be printed: "))
bizzbuzz(n)