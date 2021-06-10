
input = input("Enter a sentence : ")
word = max(input.split(" "), key = len)
largest = len(word)

print("The largest word is {} and its length is {}".format(word,largest))

