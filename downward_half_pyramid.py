#Print downward Half-Pyramid Pattern with Star (asterisk) * * * * * * * * * * * * * * *
def pyramid(n):

    for i in range(n, 0,-1):

     

        # inner loop to handle number of columns

        # values changing acc. to outer loop

        for j in range(1, i+1):

         

            # printing stars

            print("* ",end="")

      

        # ending line after each row

        print("\r")
        

n = 5
pyramid(n)
