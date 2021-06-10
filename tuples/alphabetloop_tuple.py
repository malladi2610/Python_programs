"""
Generate the tuple as follows
2)t2 = ('a','bb','ccc','dddd', .....)
"""

# output_list = []
# count = 1
# for i in range(ord('a'),ord('z')+1):
#     output_list.append(chr(i)*count)
#     count += 1
#     if(count == 27):
#         break
# output = tuple(output_list)               
# print(output)

# output = ''
count = 1
# for i in range(ord('a'),ord('z')+1):
#     output = tuple(chr(i)*count + output)
#     count += 1         

output = tuple(chr(i)*(count+1) for i in range(ord('a'),ord('z')+1))
print(output)