from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'garlic', 'onion', 'sausage')

#renames the func 'make_pizza' to 'mp' in this program. Anytime we want to call 'make_pizza' we can simply write 'mp' instead, and Pyt will run the code in 'make_pizza' while avoiding any confusion w/ another 'make_pizza' func you might have written in this program file.
