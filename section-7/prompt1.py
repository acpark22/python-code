prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# first line assigns the first part of the message to the variable 'prompt'. In the second line, the operator += takes the string that was assigned to 'prompt' and adds the new string onto the end.  The prompt now spans two lines, again with the space after the question mark for clarity
