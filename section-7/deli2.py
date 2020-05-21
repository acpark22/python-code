sandwich_orders = ['blt', 'turkey', 'pastrami', 'blt', 'pastrami', 'ham', 
        'pastrami', 'ham']
finished_sandwiches = []
print("Sorry but we are out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")



