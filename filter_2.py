# list of cities
cities = ('Madrid', 'Valencia', 'Barcelona', 'Munich', 'Stuttgart')

# cities that start with M or V
print(tuple(filter(lambda x: x.startswith(('M', 'V')), cities)))
# ('Madrid', 'Valencia', 'Munich')