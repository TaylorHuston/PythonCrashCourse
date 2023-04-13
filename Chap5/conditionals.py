cars = ['audi', 'bmw', 'subaru', 'toyota']

for cars in cars:
    if cars == 'bmw':
        print(cars.upper())
    else:
        print(cars.title())

car = 'Audi'
car.lower() == 'audi' #True

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!") #Hold the anchovies!

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!") #That is not the correct answer. Please try again!

age = 19
age < 21 #True 
age <= 21 #True
age > 21 #False
age >= 21 #False

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 #False
age_1 = 22
age_0 >= 21 and age_1 >= 21 #True
age_1 = 18
age_0 >= 21 or age_1 >= 21 #True
age_0 = 18
age_0 >= 21 or age_1 >= 21 #False

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings #True
'pepperoni' in requested_toppings #False

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#Alternate
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.") #Marie, you can post a response if you wish.

game_active = True
can_edit = False

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
printf(f"Your admission cost is ${price}.") #Your admission cost is $25.

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")