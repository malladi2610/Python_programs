"""Write a program to create a list of numbers from 1 to 50 named list_1. The numbers should be present in the increasing order: 
Ex list_1 = [1,2,3,4,5,....,50] i. e. index zero should be 1, index one should be 2, index two should be 3 and so on. 
Given an input let's say a, you have to print the number of elements of list_1 which are divisible by a, excluding the 
element which is equal to a. Ex: a=14 output=2"""

        
def divisibility(a):
    list_1 = []
    count = 0
    for i in range(1,51):
        list_1.append(i)
            
    for i in list_1:
        if(i%a == 0):    
            if(i == a):
                continue         
            count += 1
    return count
        
a = int(input("Enter the number :"))
count = divisibility(a)        
print("The no of elements divisible by", a, "in the list in", count)