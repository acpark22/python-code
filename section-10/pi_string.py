filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#start by opening the file and storing each line in a list
#create a variable 'pi_string' to hold the digits of pi. we then create a loop that adds each line of digits to pi_string and removes whitespace.
# we then print this string and also show how long the string is.


