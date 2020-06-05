with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#the open() func has one arg, the name of file you want open
#'with' closes the file once access to it is no longer needed.
#Pyt assigns it as 'file_object' which well work w/ later in program.
#'read()' meth reads the entire contents of file and stores it as one long string in 'contents'. 

