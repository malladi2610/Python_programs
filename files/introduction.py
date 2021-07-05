#Files

#Datasets used
#1. examples.txt
#2. mbox-short.txt

#Read a file
"""

a = open("files/example.txt")
print(a.read())         #By default all the content of the files are displayed

print(a.read(5))         #Returns the starting 5 char

print(a.readline())        #Reads the first line of the file

b = ("files/example.txt").read()
print(b)
"""

# Reading through the file using a loop
"""
a = open("files/example.txt")
for i in a:
    print(i)
"""

# Closing the file
"""
a = open("files/example.txt")
print(a.readline())
a.close()
"""


#Append a file
"""

a = open("files/example.txt","a")
a.write("This is my first line")
a.close()

#Now to read the file
a = open("files/example.txt","r")
print(a.read())
"""
#Write to a file(To over write)
"""
a = open("files/example.txt","w")
a.write("This is my first line")
a.close()

#Now to read the file
a = open("files/example.txt","r")
print(a.read())
"""

#Creating a file by taking input from the user
"""
a = open("files/myself.txt",'w')
name = input("Enter your name : ")
a.write(name)
a.close()
"""
#Creating a file to store a group of data in it
"""
a = open("files/student_list.txt",'a')
num = int(input("Enter the number of students in the class :"))
for i in range(num):
    name = input("Enter the name of student: ")
    a.write(name)
    a.write("\n")
a.close()
"""

#To store a group of data in it using lists by using writelines
"""
stu_list = []
a = open("files/student_list.txt",'a')
num = int(input("Enter the number of students in the class :"))
for i in range(num):
    name = input("Enter the name of student: ")
    stu_list.append(name + "\n")
a.writelines(stu_list)    #This function can be used only with list datatype
a.close()
"""

#Searching through a file
"""
fhand = open('files/mbox-short.txt')
for line in fhand:
    line = line.rstrip()          #Used to remove the space from the lines
    if line.startswith('From:'):  #No space after from
        print(line)
        
"""

#Finding a particular string in the file
"""
fhand = open('files/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)
""" 
   
#Debugging of the python file

fhand = open('files/mbox-short.txt')
fread = fhand.read()
print(repr(fread))              #It prints the files with all the special characters which are not visible