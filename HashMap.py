stock_price = {}
with open('stock_list.csv', 'r') as f:
    #print(f.read())
    for line in f:
        tokens = line.split(',')
        stocks = tokens[0]
        price = float(tokens[1])
        stock_price[stocks] = price

print(stock_price)