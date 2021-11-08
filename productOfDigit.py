#Program to find the digital product of a given number ex: n=43 Digital product ----->4*3=12
n=int(input("Enter a number: "))
tot=1
while(n>0):
    dig=n%10
    tot=tot*dig
    n=n//10
print("The total product of digits is: ",tot)
