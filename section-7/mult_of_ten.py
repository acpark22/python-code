number = input("Please tell me your number: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number, {number} is a multiple of ten.")
else:
    print(f"\nThe number, {number} is not a multiple of ten.")
