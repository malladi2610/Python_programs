number = []
i = 0
n = int(input("Enter the number of elements to be entered in the list :"))

while i < n:
    number.append(int(input("Enter the elements : ")))
    i += 1

x = int(input("Enter the element to be searched :"))
index = number.index(x)
print("The element", x, "Found at", index + 1)