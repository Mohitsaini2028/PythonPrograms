#Program to find whether a given number is a unique number. For example, 20, 56, 9863, 145, etc. are the unique numbers while 33, 121, 900, 1010, etc. are not unique numbers
  
#reading a number from the user  
number = int(input("Enter the number you want to check: "))  
#num1 and num2 are temporary variable  
num1 = number 
num2 = number
count=0
#iterate over all digits of the number  
while (num1 > 0):  
  
    #detrmins the last digit of the number      
    r1 = num1 % 10 
    while num2 > 0:  
          
        #finds the last digit  
        r2 = num2 % 10  
        #comparing the last digit  
        if r1 == r2:  
         
            #increments the count variable by 1      
            count+=1 
         
        #removes the last digit from the number  
        num2 = num2 // 10 
          
    #removes the last digit from the number  
    num1 = num1 // 10 
          
if count == 1:   
        print("The number is unique.")   
else:   
        print("The number is not unique.")  
         
          
