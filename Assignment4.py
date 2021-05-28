"""
Write a program that accepts a sentence and calculate the number of 
letters and digits.
"""

sentence = input('Enter the sentence whose characters needs to be calculated: ')
alphabets = 0
numbers = 0
specialcharacters = 0
for i in sentence:
    if(i.isalpha()):
        alphabets += 1
    elif(i.isdigit()):
        numbers += 1
    else:
        specialcharacters += 1

print("Letters - ", alphabets)
print("DIGITS - ", numbers)
print("Special character - ", specialcharacters)
        