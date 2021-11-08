#Print the following pattern* * * * * * * * * * * * * * * * * * * * * * * *

def pyramid(n):

    # outer loop to handle number of rows

    # n in this case

    for i in range(0, n):

     

        # inner loop to handle number of columns

        # values changing acc. to outer loop

        for j in range(0, i+1):

         

            # printing stars

            print("* ",end="")

      

        # ending line after each row

        print("\r")

    for i in range(n-1, 0,-1):

     

        # inner loop to handle number of columns

        # values changing acc. to outer loop

        for j in range(1, i+1):

         

            # printing stars

            print("* ",end="")

      

        # ending line after each row

        print("\r")
        
 
# Driver Code

n = 5
pyramid(n)
