alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x position: {alien_0['x_position']}")

# to modify value such as an alien moving positions and tracking it.
