import car

my_mazarati = car.Car('mazarati', 'roadster', 2000)
print(my_mazarati.get_descriptive_name())

my_volt = car.ElectricCar('chevy', 'volt', 2013)
print(my_volt.get_descriptive_name())

#importing an entire module and accessing the classes thru 
# module_name.ClassName syntax.

# you can also import every class from a module using the following syntax,
# from module_name import *

