class User:
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}\nUsername: {self.username}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}!")

class Privileges:
    def __init__(self):
         self.privileges = ['reset password', 'can add post', 'can ban user'] 
    def show_privileges(self):
        print(f"You have the following admin privileges: {self.privileges}")


class Admin(User):
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privilege = Privileges()

gary = Admin('jerry', 'garcia', 'cherry_garcia')
gary.describe_user()

gary.privilege.show_privileges()



