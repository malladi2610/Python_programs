
input = input("Enter a sentence : ")
input = input.split(" ")
str_len = []
for i in input:
    str_len.append(len(i))
largest = max(str_len)
index = str_len.index(largest)
word = input[index]
print("The largest word is {} and its length is {}".format(word,largest))

