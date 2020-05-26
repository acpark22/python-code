def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design.
    Move each design.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# the slice notation '[:]' makes a copy of the list to send to the func. If we didnt want to empty the list of unprinted designs, we could call 'print_models() like this: print_models(unprinted_designs[:], completed_models)


