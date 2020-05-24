unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#starts w/ a list of designs that need to be printed and an empty list called 'completed_models' that each design will be moved to after it has been printed. as long as designs remain in 'unprinted_designs', the 'while' loop simulates printing each design by removing a design from the end of the list, storing it in 'current_design', and displaying a message that the current design is being printed. it then adds the design to the list of completed models. when the loop is finished running, a list of the designs that have been printed is displayed.
