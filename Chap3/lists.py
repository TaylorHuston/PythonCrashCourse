bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')
print(motorcycles) #['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles) #['ducati', 'honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles) #['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()
print(motorcycles) #['honda', 'yamaha']
print(popped_motorcycle) #suzuki

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) #['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles) #['honda', 'yamaha', 'suzuki']

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) #['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)
print(cars) #['toyota', 'subaru', 'bmw', 'audi']

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) #['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars) #['subaru', 'toyota', 'audi', 'bmw']
print(len(cars)) #4

print(cars[-1]) #bmw