# Find Factorial using Recursion
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result
print("Factorial of 4:",factorial(4))
print("Factorial of 5:",factorial(5))
print("Factorial of 6:",factorial(6))
