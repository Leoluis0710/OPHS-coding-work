cars = []
x = True
while x == True:
    brand = input('plaese enter a car brand or press x to exit')
    cars.append(brand)
    print(cars)
    if cars == 'x':
        x == False
        print('exiting...')
