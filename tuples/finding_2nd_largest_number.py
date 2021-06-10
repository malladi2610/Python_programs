input = tuple(input("Enter the tuple : ").split())
n = len(input)
max_num = max(input)
sort_input = sorted(input)
print(sort_input)
second_largest_num = sort_input[-2]
print(second_largest_num)