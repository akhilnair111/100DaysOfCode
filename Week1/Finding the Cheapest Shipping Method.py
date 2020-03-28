def ground_shipping(weight):
  if weight <= 2:
    cost = weight * 1.50 + 20
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 3.00 + 20
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 4.00 + 20
    return cost
  else:
    cost = weight * 4.75 + 20
    return cost
  
print(ground_shipping(8.4))
premium_ground_shipping = 125
print("Premium groung shipping, Flat charge: $125.00")

def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50 + 0.00
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight * 9.00 + 0.00
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight * 12.00 + 0.00
    return cost
  else:
    cost = weight * 14.25 + 0.00
    return cost
  
print(drone_shipping(1.5))



def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_ground_shipping
  
  if ground < drone and ground < premium:
    return "Ground shipping is the cheapest method of shipping a "+ str(weight) + " pound package and would cost $" + str(ground)
  elif drone < ground and drone < premium:
    return "Drone shipping is the cheapest method of shipping a "+ str(weight) + " pound package and would cost $"+ str(drone)
  else:
    return "premium shipping is the cheapest method of shipping a "+ str(weight) + " pound package and would cost $" + str(premium)
    
    
    
print(cheapest_shipping(4.8))

print(cheapest_shipping(41.5))