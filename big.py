# Python Program to Find the Biggest Number using if-elif-else
# Taking First Number Input
num1 = eval(input("Enter first Number: "))
# Taking Second Number Input
num2 = eval(input("Enter second Number: "))
# Taking Third Number Input
num3 = eval(input("Enter third Number: "))
# checking weather num1>num2 and num1>num3
if num1>num2 and num1>num3:
	print("Biggest Number: ",num1)
# checking weather num2>num3
elif num2>num3:
	print("Biggest Number: ",num2)
# This will be last if it is greater this statement will be print
else:
	print("Biggest Number: ",num3)
