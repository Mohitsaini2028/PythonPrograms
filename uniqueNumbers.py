#Write a program to input 8 numbers from the user and display all the unique numbers (once).

numbers = []
while(len(numbers)<8):
    numbers.append(input("Enter Number : "))
    
print(set(numbers))
