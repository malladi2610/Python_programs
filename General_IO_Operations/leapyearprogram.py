year = int(input("Enter a year: "))

def isLeap(year):
    
    if(year % 4 == 0):
        test1 = 1
     
    elif(year % 4 != 0):
        test1 = 0
    

    if(year % 100 == 0):
        
        test2 = 0
    
    elif year % 100 != 0:
        test2 = 1
     

    if(year % 400 == 0):
        test3 = 1
    
    elif(year % 400 != 0):
        test3 = 0
    
    if(test1 and (test2 or test3)):
        print("Leap year.")
    
    else:
        print("Not leap year.")
    
isLeap(year)