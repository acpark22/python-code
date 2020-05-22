def describe_pet(pet_name, animal_type='dog'):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='rocket', animal_type='bird')

# Bc an explicit arg for 'animal_type' is provided, Pyt will ignore the parameter's default value.
