"""
Write a python code with dictionary to accept USN and Marks obtained, 
find minimum, maximum and students USN who have scored in the range on 
100 - 85, 85-75,below 60 respectively
"""

d = {}
above85 = ""
above75 = ""
above60 = ""
below60 = ""

n = int(input("Enter the no.of students in the class :"))

for i in range(n):                                              #The loop used to create the input dictionary
    d_keys = input("Enter the USN for the student : ")
    d_values = int(input("Enter the Marks for the student : "))
    d[d_keys] = d_values
    
for k,v in d.items():
    if(v >= 85):
        above85 = above85 + k + "\n"        
    if(v > 75 and v < 85):
        above75 = above75 + k + "\n"
    if(v > 60 and v < 75):
        above60 = above60 + k + "\n"          
    if(v < 60):
        below60 = below60 + k + "\n"
            
max_marks = max(d.values())
min_marks = min(d.values())
      
print("The maximum marks obtained :", max_marks)
print("The minimum marks obtained :", min_marks)
print("The Students scored between 100-85 are:")
print(above85)
print("The Students scored between 84 - 75 are:")
print(above75)
print("The Students scored between 60 - 74 are:")
print(above60)
print("The Students scored below 60 are:")
print(below60)
