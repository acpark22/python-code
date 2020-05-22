def describe_pet(pet_name, animal_type='dog'):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='rocket')

# set the default value of 'animal_type' to 'dog', now anyone calling 'describe_pet' for a dog can omit that info.
# we changed the def of 'describe_pet()' to include a default value, 'dog' for animal_type. Now when the function is called with no animal_type specified, Pyt knows to use the value 'dog' for this parameter.
# Note that the order of the parameters in the func def had to be changed, bc the default value makes it unnecessary to specify a type of animal as an argument, the only argument left in the func call is the pet's name. Pyt still interprets this as a positional arg, so if the func is called w/ just a pet's name, that arg wil match up w/ the first parameter listed in the func's definition.  This is the reason the first parameter needs to be pet_name.
