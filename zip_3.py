# list of products
products = ['table', 'chair', 'sofa', 'bed', 'lamp']

# list of prices
prices = [50, 20, 200, 150, 10]

# create a dictionary from two lists
print(dict(zip(products, prices)))
# {'table': 50, 'chair': 20, 'sofa': 200, 'bed': 150, 'lamp': 10}