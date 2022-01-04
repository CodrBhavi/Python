# Python Program to find the length of a list
# Taking Input from user
list_input = []
n = int(input("Enter a the number of elements: "))
for i in range(0,n):
    ele = int(input())
    list_input.append(ele)
print(list_input)
# Printing the length of the list
final_list = len(list_input)
print("The length of the list: ",final_list)
# End Program