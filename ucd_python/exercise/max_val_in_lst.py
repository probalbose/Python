# Start typing your code below
# Constraints:
# 1. Asks me to enter numbers over and over until I enter "0"
# 2. When I enter in "0", the program should stop and tell me the biggest number I wrote

# Defining an empty list
lstOfNums = []

# Starting a while loop to take inputs of numbers
while True:
  # This is to hadle the error in case the input is not a number
  try:
    num = int(input("Enter a number: "))
    # Breaking the loop when input is 0
    if num == 0:
      break
    # Appending the inputs into the list
    lstOfNums.append(num)
    
    # Defining a variable for the maximum value in the list then running a for loop to exract the max value 
    maxVal = lstOfNums[0]
    for i in lstOfNums:
      if i > maxVal:
        maxVal = i
      #print(maxVal)
    
  except ValueError:
    print("Sorry, that's not a number.")

# Printing the list of inputs and the max value
print(lstOfNums)
print(maxVal)
