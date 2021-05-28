##S(> 90 ),A(80 - 90),B(70-80),C(50-60),D(40 - 50) and F(<35)

name = input("Enter the name of the Student: ")
marks = int(input("Enter the marks of the Student: "))

if marks > 90:
    grade = "S"
    print("Student " + name + ", \n" + "with marks " + str(marks) + "\nhas been alloted " + grade )

elif (marks <90 and marks > 80):
    grade = "A"
    print("Student " + name + ", \n" + "with marks " + str(marks) + "\nhas been alloted " + grade )
    
elif (marks <80 and marks > 70):
    grade = "B"
    print("Student " + name + ", \n" + "with marks " + str(marks) + "\nhas been alloted " + grade )

elif (marks <60 and marks > 50):
    grade = "C"
    print("Student " + name + ", \n" + "with marks " + str(marks) + "\nhas been alloted " + grade )
    
elif (marks <50 and marks > 40):
    grade = "D"
    print("Student " + name + ", \n" + "with marks " + str(marks) + "\nhas been alloted " + grade )

elif marks<35:
    grade = "F"
    print("Student " + name + ", \n" + "with marks " + str(marks) + "\nhas been alloted " + grade )

