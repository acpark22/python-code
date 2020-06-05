filename = 'pi_digits.txt'
with open (filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# this example stores the lines of 'pi_digit.txt' in a list inside the 'with'block and then prints the lines outside the 'with' block.

# the 'readlines()' method takes each line from the file and stores it in a list. this list is then assigned to 'lines', which we can continue to work w/ after the 'with' block ends. 
# we then use a simple 'for' loop to print each line from 'lines'. bc each item in 'lines' corresponds to each line in the file, the output matches the contents of the file exactly.
