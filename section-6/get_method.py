alien_0 = {'color':'green', 'speed':'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# you can use the get() method to set a default value that will be returned if the requested key doesnt exit. The get() method requires a key as a first argument. As a second optional argument, you can pass to be returned if the key doesnt exist.
