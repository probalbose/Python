types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

# in the below line we are formatting the string and passing variable as part of the string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

hilarious = False
joke_evaluation = "Isn't that joke funny?! {}"

# in below line we will format the string and pass variable within it
print(joke_evaluation.format(hilarious))

w = "This is left side of..."
e = "a string with a right side."

print(w + e)