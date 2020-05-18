favorite_languages = {
    'joe' : 'python',
    'bob' : 'ruby',
    'ed' : 'c',
    'sue' : 'python',
    }
for name in favorite_languages.keys():
    print(name.title())

# the 'for' line tells python to pull all the keys from the dictionary 'favorite_languages' and assign them one at a time to the variable 'name'. The output shows the names of everyone who took the poll.
