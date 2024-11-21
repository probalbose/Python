def list_to_string(lst):          
    # using replace() to replace the last value of the list with 'and' + last value of the list
    new_list = [v.replace(lst[-1], "and " + lst[-1]) for v in lst]
    
    # using join() to convert the list into string with ', ' delimiter
    str = ', '.join(new_list)
    print(str)

spam = ['apple', 'banana', 'orange', 'cherry']
nospam = []
list_to_string(spam)
list_to_string(nospam)