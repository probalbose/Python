import re

lstOfNames = []

while True:
  try:
    name = input("Enter a name: ")

    # Here we are checking that the names entered are always a string
    if not re.fullmatch(r"[A-Za-z]+", name):
      raise ValueError(f"Invalid input: '{name}' contains invalid characters.")

    # Here we are breaking the loop is done is entered
    if (name == 'Done' or name == 'done'):
      break
    
    # Appending the list
    lstOfNames.append(name)
    
  except ValueError as e:
    print(f"Error: {e}, please try again.")

[print("Hello ", name) for name in lstOfNames]
