def isPowerOfTwo(n):                #User defined function for verification of the condition
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2              #Floor division divides 
                                    #Divides and returns the integer value of the quotient. 
                                    #It dumps the digits after the decimal
             
    return True
#Main Code
x = int(input("Enter the number to be tested : "))
if(isPowerOfTwo(x)):
    print('Yes')
else:
    print('No')
