formatter = "{} {} {} {}"

"""
now we will call format fucntion on 
formatter and pass variable which will
then replace the {} in formatter.

"""
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format("True",False,False,True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I want to learn",
    "Python codeing",
    "and want to become efficent",
    "and fluent in writing code"
))
    

