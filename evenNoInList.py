#Python program to find the even numbers in a List.
list1 = [11,23,45,23,64,22,11,24]
# lambda exp.
even_no = list(filter(lambda x: (x % 2 == 0), list1))
print("Even numbers in the list: ",even_no)
