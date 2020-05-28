class User:
    """An attempt to model users."""

    def __init__(self, first_name, last_name, email, age):
        """Initialize first and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def describe_user(self):
        """To describe the user."""
        print(f"\n{self.first_name.title()} {self.last_name.title()} is {self.age} years old, email at {self.email}.")
        
    def greet_user(self):
        """To greet the user."""
        print(f"\nHello, {self.first_name.title()} {self.last_name.title()}!")

ed_jones = User('ed', 'jones', 'ejones@gmail.com', 21)
ed_jones.describe_user()
ed_jones.greet_user()



