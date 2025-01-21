# Data structure exercise

import re

items = {
  "apples": 2.5,
  "bananas": 1.5,
  "pears": 1,
  "beef": 4,
  "milk": 2.5,
  "newspaper": 2
  }
  
def costOfProducts():
  
  totalCost = 0
  
  while True:
    products = input("What would you like to buy? ").strip().lower()
    
    # Making sure that the product names do not have any numerical character
    if not re.fullmatch(r"[A-Za-z]+", products):
      raise ValueError(f"Invalid input: {products} contains invalid characters.")

    if (products == 'Done' or products == 'done'):
      print("Thank you, come again soon.")
      break
    
    # This loop calculates the values of the product based on quatity and then the total cost of puschase.
    if products in items:
      try:
        quantity = float(input("How many? ").strip())
        
        cost = items[products] * quantity
        print(f"OK, that will be {cost} Euros")
        
        totalCost += cost
        #print(f"Your total bill is {totalCost}.")
      
      except ValueError as e:
        print(f"Error: {e}, quantity should be numerical.")
    
    else:
      print(f"Sorry, we do not have {products}")
  
  print(f"Your total bill is {totalCost}.")
    
costOfProducts()
