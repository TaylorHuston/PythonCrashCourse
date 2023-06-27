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

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0) #{'color': 'green', 'points': 5}

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.") #The alien is now yellow.


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the aliend based on it's current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else :
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}") # New position: 2


alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0) #{'color': 'green'}

alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points']) #KeyError: 'points'

point_value = alien_0.get('points', 'No point value assigned.') #set default value
print(point_value) #No point value assigned.

print("\n")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
"""
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
"""

print("\n")

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} #Create 30 aliens
    aliens.append(new_alien)

for alien in aliens[:3]: #Change the first 3 aliens
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]: #Show the first 5 aliens
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}") #Total number of aliens: 30