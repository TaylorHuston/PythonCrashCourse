magicians = ['alice', 'david', 'carolina']
for magician in magicians:
        print(f"{magician.title()}, that was a great trick!")
"""
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
"""

print("Thank you, everyone. That was a great magic show!") #Thank you, everyone. That was a great magic show!

for value in range(1, 5):
    print(value)

"""
1
2
3
4
"""

for value in range(5):
    print(value)

"""
0
1
2
3
4
"""

numbers = list(range(1, 6))
print(numbers) #[1, 2, 3, 4, 5]


even_numbers = list(range(2, 11, 2))
print(even_numbers) #[2, 4, 6, 8, 10]


squares = []
for value in range(1, 11):
     square = value ** 2
     squares.append(square)

print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares = [value**2 for value in range(1, 11)]
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) #0
print(max(digits)) #9
print(sum(digits)) #45

one_million = list(range(1, 1000001))
print(min(one_million)) 
print(max(one_million)) 
print(sum(one_million)) 


#Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #['charles', 'martina', 'michael']
print(players[:4]) #['charles', 'martina', 'michael', 'florence']
print(players[2:]) #['michael', 'florence', 'eli']
print(players[-3:]) #['michael', 'florence', 'eli']

for player in players[:3]:
    print(player.title())

"""
Charles
Martina
Michael
"""

#Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")    
print(my_foods)     #['pizza', 'falafel', 'carrot cake', 'cannoli']

print("\nMy friend's favorite foods are:")
print(friend_foods) #['pizza', 'falafel', 'carrot cake', 'ice cream']

list_reference = my_foods #makes a reference to the list, not a copy or new one
print(list_reference) #['pizza', 'falafel', 'carrot cake', 'cannoli']