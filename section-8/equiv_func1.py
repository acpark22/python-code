# to show that you can use different funcs that do the same thing

def describe_pet(pet_name, animal_type='dog'):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# the following for a dog named Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# the following 3 for a hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

