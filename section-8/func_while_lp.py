def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# to use 'get_formatted_name() func' w/ a 'while' loop to greet more formally. Also uses 'input'.
# first use a 'get_formatted_name(), the 'while' loop asks the user to enter their name, and we prompt for their first and last name separately.
# We add a message that informs the user how to quit, and then break out of the loop if the user enters the quit value at either prompt. 
