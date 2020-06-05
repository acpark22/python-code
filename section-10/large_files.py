filename = 'pi_mil_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

large_files = ''
for line in lines:
    large_files += line.strip()

print(f"{large_files[:52]}...")
print(len(large_files))

#pi with a million digits, we want to go read thru all and print the first 50 decimals after .


