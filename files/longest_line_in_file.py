
longest = ""
longest_list = []
# file_name = input("Enter the name of the file : ")
# a = open("files/"+file_name,"a+")

a = open("files/students_data.txt")
print(a.read())

for line in a:
    longest_list.append(line)
print(longest_list)   
# print(max(longest_list))