alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color']) #green
print(alien_0['points']) #5 

new_points = alien_0['points']
print(f"You just earned {new_points} points!") #You just earned 5 points!

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) #{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

alien_0 = {}
print(alien_0) #{}

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) #{'x_position': 0, 'y_position': 25}
