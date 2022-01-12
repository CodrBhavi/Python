# Command Line Argument from sys using argv library
from sys import argv
print("Enter Command Line Argument: ",len(argv))
print("The list of argv",argv)
print("The arguments one by one")
for i in argv:
	print(i)
	