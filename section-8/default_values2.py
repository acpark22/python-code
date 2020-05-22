def describe_pet(pet_name, animal_type='dog'):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')

# the only arg provided is 'willie' so its matched up w/ the first parameter in the definition, 'pet_name'. Bc no arg is provided for 'animal_type', Pyt uses the default value 'dog'.


