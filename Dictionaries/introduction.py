#Declaration of Dictionaries

employee = {'name' : 'john', 'company' : 'abc', 'salary' : 100000,'age' : 20}
#print(employee)

q = dict(name = 'john', comp = 'abc')
#print(q)

#Here the list is converted to dictionaries(used when the key values are present)
w = dict([['name','john'],['company','abc'],['sal',100000]])
#print(w)

#Here the tuple is converted to dictionaries
w = dict((('name','john'),('company','abc'),('sal',100000)))
#print(w)

#Adding elements and changing to the dict
q['name'] = 'ben'
q['salary'] = 100000
q['age'] = 30
#print(q)

#Displaying the elements

"""
#Printing the indices
for i in q:
    print(i)

#printing the values

for i in q:
    print(q[i])   

#printing both indices and values

for i in q:
    print(i,q[i])  
"""
    
#Displays the list of keys

"""
print(list(q.keys()))

print(list(q.values()))

a = list(q.keys())
print(a[0])
"""

#Display the list of the items in the dictionary

print(q.items())   #This gives the data in iteratable format in terms of Keys and values
