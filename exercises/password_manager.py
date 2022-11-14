import os
import random


print('Welcome to The ultimate Password Manager: ')
print('What do you wanna do? ')
query= input("type 'a' to add password, "+"\n"+"'v' to view existing ones and "+"\n"+"'g' to generate a random password: ").lower()

def input_checker(value):
  if value== 'g':
    return generate_passwd()
  elif value=='v':
    pass
  elif value=='a':
    pass
  else:
    return "\n" + 'Invalid Input'
  

def generate_passwd():
  numbers= '123456789'
  characters= '~!@#$%^&*()__+/*-?:"'

  def generator(value):
    return 'hello'

  print('Enter a random word.We will build your secure password from there... ')
  query_2= input('Take Note: This is not your password.It only helps us to generate a strong one: ').lower()
  while True:
    if len(query_2)<8:
      print('Word Too Weak ! ')
      query_3= input('enter a stronger word! At least 9 characters for extra security: ').lower()
      if len(query_3)<8:
        return "You've failed to Follow Instructions! "
        break
      else:
        print("\n"+ '...........verification successful!')
        print( '...........your password is being generated ' + "\n" )
        return generator(query_3)
        break
    else:
      print("\n"+'...........verification successful!')
      print( '...........your password is being generated ' + "\n" )
      return generator(query_2)
      break
   

print(input_checker(query))
