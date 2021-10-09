# Write a program to print the following star pattern:
#   *
#  * *
# * * * for n =3



# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

n = 3
triangle(n)
