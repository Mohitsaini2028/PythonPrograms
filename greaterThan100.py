#Given two integer numbers return their sum. If the sum is greater than 100, then return their product
f=int(input("Enter first number :"))
s=int(input("Enter second number :"))

addition=f+s
print("sum is : ",addition)

if(addition>100):
    print("Product is : ",f*s)
