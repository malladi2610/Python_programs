"""
Generate the tuple as follows
2)t2 = ('a','bb','ccc','dddd', .....)
"""
#Using the concept of lists

output_list = []
count = 1
for i in range(ord('a'),ord('z')+1):
    output_list.append(chr(i)*count)
    count += 1
    if(count == 27):
        break
output = tuple(output_list)               
print(output)

       
#Using the concept of tuples
output = tuple(chr(i)*(i-96) for i in range(ord('a'),ord('z')+1))
print(output)