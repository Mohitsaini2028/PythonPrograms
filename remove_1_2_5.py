#Write a Python program to print a specified list after removing the 1st, 2nd and 5th elements.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,1,4)]
print(color)
