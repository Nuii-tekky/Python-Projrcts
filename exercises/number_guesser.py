import random

print('welcome to my game i bet you cant guess my hidden number: ')
query= int(input('enter a number between 50 and 450: '))

def guess(x):
  random_number = random.randint(1, x)
  guess= 0
  while guess != random_number:
    guess = int(input(f'guess a number between 1 and {x}: '))
    if guess < random_number:
      print('Nope!! Too low')
    elif guess > random_number:
      print('Nope!! .Too high')  

  print(f'Cant believe you guessed It.{random_number} was correct')    

if query>450:
  print('Always learn to follow instructions! ')
elif query<50:
  print('was that what i told you to type? ')
else:
  guess(query)
 
