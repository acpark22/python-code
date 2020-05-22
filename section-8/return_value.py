def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# the 'return' stmnt takes a value from inside a func and sends it back to the line that called the func. 
# the definition of 'get_formatted_name' takes as parameters a first and last name. The func combines these two names, adds a space btwn them, and assigns the result to 'full_name'. 
# The value of 'full_name' is converted to title case, and then returned to the calling line at 'return full_name.title()'
# when you call a func that returns a value, you need to provide that the return value can be assigned to. In this case, the returned value is assigned to the variable 'musician'. 
