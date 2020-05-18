favorite_cars = {
    'phil': 'bmw',
    'andy': 'audi',
    'cam': 'toyota',
    'dan': 'nissan',
    }
print("The following cars have been mentioned:")
for car in favorite_cars.values():
    print(car.title())

# the 'for' statement here pulls value from the dictionary and assigns it to the variable 'car'. 
