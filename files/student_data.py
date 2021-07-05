a = open("files/student_data.txt","a+")

num = int(input("Enter the number of students : "))

for i in range(num):
    print("Enter the USN of the student ", (i + 1)," : ")
    USN = input()
    Name = input("Enter the name of the student : ")
    CGPA = input("Enter the CGPA of the student : ")
    data = USN + "\t" + Name + "\t" + CGPA + "\n"
    a.write(data)
a.seek(0)   #It is used to get the cursor to the top of the file and start reading from there
            #If not used with "a+,w+,etc..,", then would return an empty string as the reading happens from the bottom of the page
for i in a:
    print(i)
a.close()