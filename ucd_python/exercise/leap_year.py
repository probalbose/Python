# Leap year notes
# If the year divides by 4, but not by 100, it is a leap year
# If the year divides by 4, and by 100, and by 400, it is a leap year
# If the year divides by 4, and by 100, but not by 400, it is not a leap year
# If the year doesn't divide by 4, it is not a leap year
#
# Hint:
# Use the % operator

# Creating a function to evaluate leap year
def is_leap(year):
      if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divides by 4, 100, and 400
            else:
                return False  # Divides by 4 and 100, but not 400
        else:
            return True  # Divides by 4 but not 100
      else:
        return False  # Doesn't divide by 4

# Taking an input of year
year = int(input("Enter a year: "))

# Printing if the input is a leap year
if is_leap(year):
    print("That is a leap year.")
else:
    print("Nope, not a leap year.")
