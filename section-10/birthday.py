filename = 'pi_mil_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

birthday_file = ''
for line in lines:
    birthday_file += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in birthday_file:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

#is your birthday appear anywhere in the first million digits of pi
