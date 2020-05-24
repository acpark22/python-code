def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty',  'margot']
greet_users(usernames)

#send a list of names to a function called greet_users(), which greets each person in the list individually.
#define greet_users() so it expects a list of names, which it assigns to the parameter 'names'. the func loops thru the list it recvs and prints a greeting to each user. 
#at 'usernames' we define a list of users and then pass the list 'usernames' to 'greet_users()' in our func call 

