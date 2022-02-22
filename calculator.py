''' Python Project:2 
    Simple Calculator '''
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y

print("Select an Operator for Calculation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = eval(input("Enter Operation(1/2/3/4): "))

if choice in(1,2,3,4):
    num1 = eval(input("Enter first Number: "))
    num2 = eval(input("Enter second Number: "))

if choice == 1:
    print(num1,"+",num2,"=",add(num1,num2))

elif choice == 2:
    print(num1,"-",num2,"=",sub(num1,num2))

elif choice == 3:
    print(num1,"*",num2,"=",mult(num1,num2))

elif choice == 4:
    print(num1,"/",num2,"=",div(num1,num2))

else:
    print("Invalid Operator")
