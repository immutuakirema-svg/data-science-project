#customer input
size=input('pizza size')
toppings=int(input ('number of toppings'))
distance= float(input('delivery distance'))
#determine pizza prize
if size =='small':
    price=8
elif size =='large':
 price=12
 #determine topping cost
topping_cost=toppings * 1
 #delivery fee
if distance<=5:
    deliveryfee=2
else:
    deliveryfee=1 +(2)*1
    #total cost
totalcost=price+ topping_cost+deliveryfee
#display results

print(f'Pizza size:{size}')
print(f'Topping cost:${topping_cost}')
print(f'Delivery cost: ${deliveryfee}')
print(f'Totalcost:${totalcost}')