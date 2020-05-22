def build_person(first_name, last_name):
    """Return a dictionary of info about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

# the func 'build_person()' takes in a first and last name, and puts these values into a dict.
# the value of first_name is stored w/ the key 'first', and the value of 'last_name' is stored w/ the key 'last'. The entire dict representing the person is returned.
# The return is printed at 'print(musician)' w/ the orig two pieces of textual info now stored in a dict.
