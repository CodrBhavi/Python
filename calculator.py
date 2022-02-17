''' Creating a Calculator '''
num1 = eval(input("Enter your First Number: "))
num2 = eval(input("Enter your Second Number: "))
num3 = eval(input("Enter your Expression in double inverted commas: "))
if num3 == "+":
    print("Answer:",num1+num2)
if num3 == "-":
    print("Answer:",num1-num2)
if num3 == "*":
    print("Answer:",num1*num2)
if num3 == "/":
    print("Answer:",num1/num2)

