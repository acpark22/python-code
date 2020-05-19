users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# first define a dict called 'users' with 2 keys: one each for the usernames 'aeinstein' and 'mcurie'. the value associated w/ each key is a dict that includes each user's first name, last name, and location. 
# we first loop thru the 'users' dict. Python assigns each key to the variable 'username' and the dict associated w/ each username is assigned to the variable 'user_info'. Once inside the main dict loop, we print the username 
# The we start accessing the inner dict. The variable 'user_info', which contains the dict of user info, has 3 keys: 'first', 'last', and 'location'. We use each key to generate a neatly formatted full name and location for each person, and then print a summary of what we know about each user.
