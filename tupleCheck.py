# Check that a tuple cannot be changed in python.

'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''

# Example
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "mango"
x = tuple(y)

print(x)
