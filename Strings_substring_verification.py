sen = input("Enter the Sentence to be tested on: ")
x = input("Enter the string to be checked: ")

if x in sen:
    print("The string " + x + " is present in the " + sen)
else:
    print("The entered string is not present")