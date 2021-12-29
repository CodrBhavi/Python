# Python program to interchange first and last elements in a list
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
# Driver code
newList = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	newList.append(ele) # adding the element
	
print(newList)

print(swapList(newList))
