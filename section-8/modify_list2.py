def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#we define func 'print_models(_ w/ 2 parameters: a list of designs that need to be printed and a list of completed models. Given these 2 lists, the func simulates printing each design by emptying the list of unprinted designs and filling up the list of completed models. 
#Define the func 'show_completed_models()' displays the name of each model that was printed. 
#Call 'print_models()' and pass it the 2 lists it needs; as expected, 'print_models() simulates printing and designs. Then we call 'show_completed_models()' and pass it the list of completed models so it can report the models that hve been printed. the descriptive func names allow others to read this code and understand it, even w/o comments.

