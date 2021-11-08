#Python program to delete an element from a list by index which is given by the user.

myList = ["Mohit",7.0,"car",46,18,True]
print(myList)
index = int(input("Enter the Index of Element you want to remove: "))
myList.pop(index)
print("After Removal : ",myList)
