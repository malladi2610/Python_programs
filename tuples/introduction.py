#Creation of Tuples

"""
t1 = (2,3,4,'a','zero')
s = ["python", "is", "good", 1]
l1 = list(s)
print(l1)
t2 = tuple(l1)
print(t2)
"""

#Creation from the user input

#By using split
"""
t3 = tuple(input("Enter the elements : ").split()) #tuple() is used as the output of split is always list
print(t3)
"""

#By using eval
"""
t4 = eval(input("Enter the elements : "))  #The input needs to be given in the form of data to be displayed it i.e {}(Dict), [](list), ()(tuple)
print(t4)
"""

#Printing the tuples
#As they are immutable like strings, So travesal is used for printing

t = ('a', 'e', 'i', 'o')
for i in t:
    print(i)
    
#Operation on tuples
#Similar to Strings

#Concatenation
"""
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)
"""

#Duplication
"""
t3 = t3*3
print(t3)
"""

#Slicing
t5 = (1,2,3,4,5,6,7,8,9,1,6)
print(t5[0::2])
print(t5[1::2])
print(t5[::-1])