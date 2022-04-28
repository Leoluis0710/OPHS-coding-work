cars = []
x = True

while x == True:
    x = input('plaese enter a car brand or press x to exit')
    cars.append(x)
    print(cars)
    if x == 'x':
        x == False
        print('exiting...')
    else:
        x = True
