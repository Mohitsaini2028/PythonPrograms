#Create an outer function that will accept three parameters, a, b and c. Create an inner function inside an outer function that will calculate the addition of a, b and c. At last, an outer function will add 5 into addition and return it

def outer(a,b,c):
    def inner(a,b,c):
        return a+b+c
    return inner(a,b,c)+5

print(outer(4,6,8))
