filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#assign the name of file to 'filename' We then call 'open()' an object respresenting the file and its contents is assigned to the variable 'file_object'
#We again use the 'with' syntax to let Pyt open and close the file properly.
#to examine the file's contents, we work thru each line in the file by looping over the file object.
