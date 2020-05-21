prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
# set the variable 'active' to True so the program starts in an active state. Doing so makes the 'while' statement simpler bc no comparison is made in the 'while' statement itself: the logic is taken care of in other parts of the program.  As long as the 'active' variable remains True, the loop will cont to run.  In the 'if' statement inside the 'while' loop, we check the value of 'message' once the user enters their input.  If the user enters 'quit', we set 'active' to False, and the 'while' loop stops.  If the user enters anything other than 'quit', we print their input as a message. 
