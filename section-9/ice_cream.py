class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name.title()
        self.cuisine = cuisine.title()
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} food.")

    def open_restaurant(self):
        print(f"Welcome to {self.name}!")

    def set_number_served(self):
        print(f"We have served {self.number_served} customers.")

    def increment_number_served(self, number_served):
        self.number_served += number_served

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['choc', 'straw', 'vanilla']

    def show_flavors(self):
        print(f"{self.name} has {self.flavors} flavored ice cream.")

my_ice = IceCreamStand('coldstone', 'gourmet ice cream')
my_ice.describe_restaurant()
my_ice.show_flavors()




