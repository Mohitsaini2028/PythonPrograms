#To check whether a number is divisible by 8 and 12 or not.

no=int(input("Enter the Number : "))

if no%8==0 and no%12==0:
    print("Number is divisible by 8 and 12")
else:
    print("Number is not divisible by 8 and 12")
