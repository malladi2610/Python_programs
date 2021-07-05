x = ('2','3','1','5','4')
x_list = list(x)  #['2','3','1','5','4']
sorted_x_list = x_list.sort() #This function will sort the list and apply the chages to x_list ['1','2','3','4','5']
x_sorted = tuple(x_list) #This will convert list to tuple
print("The sorted tuple is : ", x_sorted)  

#With Sorted function
x = ('2','3','1','5','4')
x_sorted = sorted(x)
x_sorted = tuple(x_sorted)
print(x_sorted)