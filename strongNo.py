#Program to find whether a given number is a strong number or not. e.g. n=145 1!+4!+5!==145


f = [None] * 10
 
# Fills factorials of digits from 0 to 9.

def preCompute() :

    f[0] = f[1] = 1;

    for i in range(2,10) :

        f[i] = f[i-1] * i

  
# Returns true if x is Strong

def isStrong(x) :

     

    factSum = 0

    # Traverse through all digits of x.

    temp = x

    while (temp) :

        factSum = factSum + f[temp % 10]

        temp = temp / 10
 

    return (factSum == x)

     
# Driver code
preCompute()

x = 145

if(isStrong(x) ) :

    print "Yes"

else : 

    print "No"

x = 534

if(isStrong(x)) :

    print "Yes"

else: 

    print "No"
