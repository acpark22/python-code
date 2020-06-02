class User:
    def __init__(self, first_name, last_name, email, age):
        """Initialize first and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def describe_user(self):
        msg = f"{self.first_name} {self.last_name} \nEmail: {self.email} \nAge: {self.age}"
        return msg.title()

    def greet_user(self):
        print(f"Hey {self.first_name.title()}, welcome back!")

class Admin(User):
    def __init__(self, first_name, last_name, email, age):
        super().__init__(first_name, last_name, email, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        print(f"Admin {self.first_name.title()},  has the following privileges: {self.privileges}")

my_user = User('bilbo', 'baggins', 'bbaggs@hobbit.com', 699)

my_admin = Admin('george', 'carlin', 'gcarl@smart.com', 43)
print(my_admin.describe_user())
my_admin.show_privileges()


