#Program to find digital sum of a given Number ex: n=123 Digital sum----->1+2+3=6
n=int(input("Enter a number: "))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is: ",tot)
