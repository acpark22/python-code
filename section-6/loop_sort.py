favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# wrapped the sorted() function around the dictionary.keys() method. this tells python to list all keys in the dictionary and sort that list before looping through it.
