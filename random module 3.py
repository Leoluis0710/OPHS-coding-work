import random
coin = ['heads', 'tails']
outcome = random.choice(coin)
guess = input('guess the outcome')
if guess == outcome:
    print('you win')
else:
    print('bad luck')
    print(outcome)

