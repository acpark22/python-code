prompt = "\nPlease tell me the toppings you would like on your pizza:"
prompt += "\n(Enter 'quit' when you are done with you pizza.)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"I will add {topping} to your pizza!")

