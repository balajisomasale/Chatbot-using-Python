'''Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

Premium Ground Shipping

Flat charge: $125.00

Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

Tasks
7/7Complete
Mark the tasks as complete by checking them off
Finding the Cheapest Shipping Method
7.
Great job! Now, test your function!

What is the cheapest method of shipping a 4.8 pound package and how much would it cost?

What is the cheapest method of shipping a 41.5 pound package and how much would it cost?

(See hint for answers)'''

#standard ground shipinng

def ground_shipping_cost(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else :
    price_per_pound = 4.75
  return 20 + (weight * price_per_pound)
print(ground_shipping_cost(8.4))



#premium ground shipping
premium_ground_shipping = 125.00


#Drone Shipping
def drone_shipping_cost(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else :
    price_per_pound = 14.25
  return  (weight * price_per_pound)
print(drone_shipping_cost(1.5))



#cheapest shipping method
def print_cheapest_shipping_method(weight):
  ground = ground_shipping_cost(weight)
  premium = premium_ground_shipping
  drone = drone_shipping_cost(weight)
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method ="premium ground"
    cost = premium
  else:
    method ="drone"
    cost = drone
    
  
  print(
    "The cheapest option available is $%.2f with %s shipping"
      % (cost, method)
  )
  

print_cheapest_shipping_method(4.8)
print_cheapest_shipping_method(41.5)


