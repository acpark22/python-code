class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name.title()
        self.cuisine = cuisine.title()
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine}.")

    def open_restaurant(self):
        print(f"{self.name} is open for business!")

    def set_number_served(self):
        print(f"We have served {self.number_served} customers.")

    def increment_number_served(self, number_served):
        """Add the given amount to the odometer reading."""
        self.number_served += number_served

restaurant = Restaurant('waffle house', 'gourmet food')

restaurant.number_served = 200000
restaurant.set_number_served()

restaurant.increment_number_served(500)
restaurant.set_number_served()

