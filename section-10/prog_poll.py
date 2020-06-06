filename = 'responses.txt'

answers = []
while True:
    answer = input("\nWhy do you like programming? ")
    answers.append(answer)

    continue_poll = input("Would someone else like to answer? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as file_object:
    for answer in answers:
        file_object.write(answer + "\n")

#Write a while loop that asks people why they like programming. each time someone enters a reason, add their reason to a file that stores all the responses.


