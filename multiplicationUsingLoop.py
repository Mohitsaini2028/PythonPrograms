# Write a program to print multiplication table for a given number 
# using for as well as while loop.

number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
# By using "for loop"       
print ("\nThe Multiplication Table of: ", number,"By using for loop")    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)

# By using "while loop"

count = 1        
print ("\n\nThe Multiplication Table of: ", number,"By using while loop")    
while count <= 10:    
    number = number * 1    
    print (number, 'x', count, '=', number * count)    
    count += 1  
