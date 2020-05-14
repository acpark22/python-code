user_names = ['carl', 'joe', 'dan', 'admin', 'bob']
for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello, {user_name.title()}, thanks for logging in.")
        
