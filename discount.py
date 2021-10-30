#A shop will give discount of 50% if the cost of purchased quantity is more than 10000. Ask user for quantity 
#suppose, one unit will cost 100. Judge and print total cost for user.


quantity = int(input("Enter quantity "))
if quantity*100 > 10000:
  print("Cost is",((quantity*100)-(.5*quantity*100)))
else:
  print("Cost is",quantity*100)
