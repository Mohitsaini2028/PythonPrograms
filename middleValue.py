#Write a function that returns the middle value among three integers. (Hint: make use of min() and max()). Write code to test this function with different inputs.

a=10
b=20
c=30
maximum = max(a,b,c)
minimum = min(a,b,c)

if a!=maximum and a!=minimum:
    print(a ," is middle element ")
elif b!=maximum and b!=minimum:
    print(b ," is middle element ")
elif c!=maximum and c!=minimum:
    print(c ," is middle element ")
