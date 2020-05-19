message = input("How many people in your dinner party? ")
message = int(message)

if message >= 8:
    print(f"\nYou will have to wait longer for your table.")
else:
    print(f"\nYour table is ready, please follow me.")

