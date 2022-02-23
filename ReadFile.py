""" user_map = []
with open('stock_list.csv', 'r') as f:
    for line in f:
        lst = line.split(':')
        user_id = lst[0]
        user_nam = lst[1]
        if user_id not in user_map:
            user_map.append([user_id, user_nam])


for element in user_map:
    if element[0] == 'goog':
        print(element[1]) """


user_map = []
with open('/etc/passwd', 'r') as f:
    for line in f:
        lst = line.split(':')
        user_id = lst[0]
        user_nam = lst[1]
        if user_id not in user_map:
            user_map.append([user_id, user_nam])


for element in user_map:
    if element[0] == 'goog':
        print(element[1])
    elif element[0] == 'fb':
        print(element[1])
    