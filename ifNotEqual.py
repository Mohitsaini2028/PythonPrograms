#Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum.
def sum_four(x, y, z):

     sum = x + y + z
  
     if x == y == z:
      sum = sum * 4
     return sum

print(sum_four(1, 2, 3))
print(sum_four(3, 3, 3))
