filename = 'learning_python.txt'

print("--- Reading entire file:")
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

print("\n--- Reading by looping over file object:")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print("\n--- Reading by storing lines in list:")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())




