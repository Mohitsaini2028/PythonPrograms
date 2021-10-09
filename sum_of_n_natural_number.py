# Write a program to print the sum of first n natural numbers using while loop.
num = int(input("Enter any Number "))

if num < 0:
   print("Enter a positive number Please")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
