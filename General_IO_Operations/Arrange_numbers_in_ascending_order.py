x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))
mid_num = 0
min_num = 0
max_num = 0

if x > y:
    if x > z:
        max_num = x
        if y > z:
            mid_num = y
            min_num = z
        else:
            mid_num = z
            min_nm = y
    elif x < z:
        max_num = z
        mid_num = x
        min_num = y
else:
    if y > z:
        max_num = y
        if x > z:
            mid_num = x
            min_num = z
        else:
            mid_num = z
            min_num = x
    max_num = z
    mid_num = y
    min_num = x
                
print("The numbers in ascending order are ", min_num, mid_num, max_num)
    
    