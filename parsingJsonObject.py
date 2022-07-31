import json
cart='{"pr3":[6,"JBL partyBox",10],"pr2":[1,"mi band 3",2],"pr6":[1,"speaker",500],"pr5":[1,"laptop",50000]}'
carts=json.loads(cart)
totalPrice=0
for cart in carts:
    totalPrice+=carts[cart][0]*carts[cart][2]
    
print(totalPrice)
