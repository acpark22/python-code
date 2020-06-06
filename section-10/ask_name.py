filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("What's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
            print("Hi " + name + ", you've been added to the guest book.")

#Write a 'while' loop that prompts users for their name. when they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. make sure each entry appears on a new line.

