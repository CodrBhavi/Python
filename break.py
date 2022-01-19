# Python Program example of break keyword
cart = [10,20,600,70,80]
for item in cart:
	if item>500:
		print("To place this order insurence must be required!!")
		break
	print(item)
