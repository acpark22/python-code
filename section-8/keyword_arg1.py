def describe_pet(animal_type, pet_name):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")

describe_pet(animal_type='hamster', pet_name='harry')

# when we call the func, we explicitly tell Pyt which parameter each arg should be matched with. When Pyt reads the func call, it knows to assign the arg 'hamster' to the parameter animal_type and the arg 'harry' to pet_name
