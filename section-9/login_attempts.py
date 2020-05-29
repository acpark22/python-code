class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, email is {self.email}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name} {self.last_name}!")

    def greeter_login_attempts(self):
        print(f"This user has {self.login_attempts} login attempts.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

bodie = User('bodie', 'broadus', 'bb@thewire.com')
bodie.describe_user()

bodie.login_attempts = 3
bodie.increment_login_attempts()
bodie.greeter_login_attempts()
bodie.reset_login_attempts()
bodie.greeter_login_attempts()


