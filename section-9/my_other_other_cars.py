from car import Car
from my_electric import ElectricCar

my_beetle = Car('volkswagon', 'beetle', 2008)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())

