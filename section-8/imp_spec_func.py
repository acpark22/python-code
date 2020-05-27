from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'onion', 'garlic', 'green peppers')

#to import specific function. with this syntax, you dont need to use the dot notation when you call a function bc weve explcitly imported the func 'make_pizza' in the 'import' stmnt, we can call it by name when we use the func.

#you can import as many funcs as you want from a module by sep each func's name w/ a comma:
# from module_name import function_0, function_1
