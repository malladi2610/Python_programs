d = {}      #The input Dictionary
d_ic = {}   #Dictionary obtained after interchange

def dict_generate(x):
    for i in range(x):                                              #The loop used to create the input dictionary
        d_keys = input("Enter the key value for the dictionary : ")
        d_values = input("Enter the values for the dictionary : ")
        d[d_keys] = d_values
    return d

def dict_interchange():
    d_keys = list(d.values()).copy()        #The list of values of dictionary are assigned to the keys 
    d_values = list(d.keys()).copy()        #The list of keys of dictionary are assigned to the values 
    for i in range(x): 
        d_keys_ic = d_keys[i]               #The loop used to create the interchanged dictionary
        d_values_ic = d_values[i]
        d_ic[d_keys_ic] = d_values_ic
    return d_ic

#Main Loop
x = int(input("Enter the no.of elements to be entered in the dictionary :"))

d_generated = dict_generate(x)
print("The input dictionary is :")
print(d_generated)

d_interchanged = dict_interchange()
print("The interchanged dictionary is :")
print(d_interchanged)

