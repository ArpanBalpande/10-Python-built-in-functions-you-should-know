# list of products
products = ['table', 'chair', 'sofa', 'bed', 'lamp']

# list of prices
prices = [50, 20, 200, 150, 10]

for product, price in zip(products, prices):
    print('Product: {}, Price: {}'.format(product, price))

# Product: table, Price: 50
# Product: chair, Price: 20
# Product: sofa, Price: 200
# Product: bed, Price: 150
# Product: lamp, Price: 10