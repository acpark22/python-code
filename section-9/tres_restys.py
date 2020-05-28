class Restaurant:
    """A model of restaurants."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine type attributes."""
        self.restaurant_name  = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Will print the name and cuisine attributes."""
        print(f"\n{self.restaurant_name.title()} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Will print a message that the restaurant is open."""
        print(f"\n{self.restaurant_name.title()} is now open!")

college_cafe = Restaurant('college cafe', 'chinese')
dc_oaks = Restaurant('dc oaks', 'bar')
nobu = Restaurant('nobu', 'sushi')

college_cafe.describe_restaurant()
dc_oaks.describe_restaurant()
nobu.describe_restaurant()



