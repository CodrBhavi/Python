''' Program to filter only even numbers from the list by using filter() function and lambda() function ''' 
l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l1 = list(filter(lambda x:x%2 == 0,l))
print("Even Numbers:",l1)
l2 = list(filter(lambda x:x%2 != 0,l))
print("Odd Numbers:",l2)
