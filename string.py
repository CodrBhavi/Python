# Accessing Characters in String by using Index
s = input("Enter some String: ")
i = 0
for x in s:
	print("The character index at positive {} and in negative {} is {}".format(i,i-len(s),x))
	i = i + 1
