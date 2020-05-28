class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Rocket', 5)
my_dog.sit()
my_dog.roll_over()

#after we create an instance from the class, Dog, we can use dot notation to call any method defined in Dog. 
#to make our dog sit and roll over.
