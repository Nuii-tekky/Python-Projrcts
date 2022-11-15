import os
import random
from datetime import datetime as dt

print('Welcome to The ultimate Password Manager: ')
print('What do you wanna do? ')
query= input("type 'a' to add password, "+"\n"+"'v' to view existing ones and "+"\n"+"'g' to generate a random password: ").lower()

def input_checker(value):
  if value== 'g':
    return generate_passwd()
  elif value=='v':
    return view_passwd()
  elif value=='a':
    pass
  else:
    return "\n" + 'Invalid Input'
  

def generate_passwd():
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
       
def view_passwd():
  path= r'C:\Users\ekomobong\Documents\My Projects\Python\Python-sandboxes\exercises\passwords.txt'
  if os.path.exists(path):
    with open(path,'r+') as passwd_line:
      pass
    print('Your saved passwords will now be shown: ' + "\n")
  else:
    print(' checking......................')
    print(' Oops!! No saved passwords.')
    query_4= input("You can add passwords here.just type 'a' to add or 'q' to quit: ").lower()
    if query_4=='a':
      return add_passwd()
    elif query_4== 'q':
      quit()  
    else:
      print('You failed to follow instructions! ')
      return 'Your session has been wiped out! '      
  

def add_passwd():
  return 'hello'


print(input_checker(query))
 