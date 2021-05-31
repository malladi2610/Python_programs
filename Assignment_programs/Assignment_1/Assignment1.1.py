"""Write a program which will print all such numbers which are 
divisible by 7 but are not a multiple of 5, between 2000 and 3200 
(both included)."""

starting_range = 2000
ending_range = 3200

for i in range(starting_range,ending_range+1):
    if i%7 == 0:
        if i%5 != 0:
            print(i, "", end = '')