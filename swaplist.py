# Python3 program to swap elements at
# given positions

# Swap function
def swapPositions(list, pos1, pos2, pos3, pos4):

	# Storing the two elements
	# as a pair in a tuple variable get
	get = list[pos1], list[pos2], list[pos3], list[pos4]
	
	# unpacking those elements
	list[pos4], list[pos3], list[pos2], list[pos1] = get
	
	return list

# Driver Code
List = [10, 65, 20, 90]

pos1, pos2, pos3, pos4 = 1, 3, 2, 4
print(List)
print(swapPositions(List, pos1-1, pos2-1, pos3-1, pos4-1))
