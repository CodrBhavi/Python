''' Example Program of Variable Length Argumnets in Functions '''
def fun(*n):
    total = 0
    for n1 in n:
        total = total + n1
    print("The Sum:",total)
fun()
fun(10)
fun(10,40)
