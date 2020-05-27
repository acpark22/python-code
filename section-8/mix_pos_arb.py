def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMkaing a {size}-inch pizza w/ the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'olives')

#the arbitrary args must be placed last in the func definition.
#In the func def, Pyt assigns the first value it recvs to the parameter 'size'. All other values that come after are stored in the tuple 'toppings'

