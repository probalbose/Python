import re


no_of_code_line = int(input())

color = r'^#[a-fA-F0-9]{3,6}'

# if re.match(color, '#04a89F'):
    # print("Its a match")
# else:
    # print("Not a match")

for n in range(no_of_code_line):
   
    color_input = input()
    
    if re.match(color, color_input):
        print("Its a match for: ", color_input)



