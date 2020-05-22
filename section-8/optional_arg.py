def get_formatted_name(first_name, last_name, middle_name=''):
        """Return a full name, neatly formatted."""
        if middle_name:
            full_name = f"{first_name} {middle_name} {last_name}"
        else:
            full_name = f"{first_name} {last_name}"
        return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# to make 'middle_name' optional, we can give the 'middle_name' to an empty default value and ignore the argument unless the user provides a value. To make 'get_formatted_name' to work w/o a middle name, we set the default value of 'middle_name' to an empty string and move it to the end of the list of parameters. 
# in body of func, we check to see if a middle name has been provided. Pyt interprets non-empty strings as True, so 'if middle_name' evaluates to True, if a middle name arg is in the function call.
# if a middle name is provided, the first, middle, and last names are combined to form a full name. this name is then changed to title case and returned to the func call line where its assigned to the variable 'musician' and printed. 
# Calling this function w/ a first and last name is straightforward. If were using a middle name, however, we have to make sure the middle name is the last argument passed so Pyt will match up the positional args correctly.
