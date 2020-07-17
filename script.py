def cost_ground_shipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20 + (price_per_pound * weight)   

print(cost_ground_shipping(8.4))

premium_shipping = 125

def cost_drone_shipping(weight):
  if weight <= 2:
     price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:    
    price_per_pound = 14.25

  return weight * (price_per_pound)

print(cost_drone_shipping(1.5))

def cheapest_shipping(weight):
  ground = cost_ground_shipping(weight)
  drone = cost_drone_shipping(weight)
  premium = premium_shipping

  if ground < drone and ground < premium:
      method = "ground shipping"
      cost = ground
  elif premium < ground and premium < drone:
    method = "premium shipping"
    cost = premium
  else: 
    method = "drone shipping"
    cost = drone

  print("you chose the cheapest shipping method. With %s you only pay $%.2f"
    %(method, cost)
    )
print(cheapest_shipping(4.8))

print(cheapest_shipping(41.5))
   














