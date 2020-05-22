def build_person(first_name, last_name, age=None):
    """Return a dict of info about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age= 27)
print(musician)

# we add a new optional parameter 'age' to the func definition and assign the parameter the special value 'None', which is used when a variable has no specific value assigned to it. You can think of 'None' as a placeholder value. In conditional tests, 'None' evaluates to 'False'. If the func call includes a value for 'age', that value is stored in the dict. This func always stores a person's name, but it can be modified to store any other info
