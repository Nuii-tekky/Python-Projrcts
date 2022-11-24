

import os
import random
import time

print('Welcome to The ultimate Password Manager: ')
print('What do you wanna do? ')
query= input("type 'a' to add password, "+"\n"+"'v' to view existing ones and "+"\n"+"'g' to generate a random password: ").lower()

def input_checker(value):
  if value== 'g':
    return generate_passwd()
  elif value=='v':
    return view_passwd()
  elif value=='a':
    return add_passwd()
  else:
    return "\n" + 'Invalid Input'
  

def generate_passwd():
  def generator(value):
    password= ''
    chars= f'{value.upper()}{value}1234567890~!@#$%&*'
    for char in range(10):
      password += random.choice(chars)
    complete_word_list= list(password)
    random.SystemRandom().shuffle(complete_word_list)
    password= ''.join(complete_word_list)  
    return f'your random password is: {password}'

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
        time.sleep(1)
        print( '...........your password is being generated ' + "\n" )
        time.sleep(2)
        return generator(query_3)
        break
    else:
      print("\n"+'...........verification successful!')
      time.sleep(1)
      print( '...........your password is being generated ' + "\n" )
      time.sleep(2)
      return generator(query_2)
      break
       
def view_passwd():
  passwd_path= r"C:\Users\ekomobong\Documents\PDF'S\passwords.txt"
  if os.path.exists(passwd_path):
    with open(passwd_path,'r') as passwd_file:
      for line in passwd_file.readlines():
        print("\n" + line.rstrip())
        return ' there you go...'
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
  passwd_path= r"C:\Users\ekomobong\Documents\PDF'S\passwords.txt"
  print(f'\n Safeguard your passwords here... ')
  query_5= input(' enter the account or username associated with this: ').lower()
  if len(query_5)>= 1:
    query_6= input(' enter the password: ')
  else:
    print('\n'+' Username skipped! ')
    query_6= input(' enter the password: ') 
  with open(passwd_path,'a') as file:
    if len(query_5)>=1:
      file.write(f'Username/Account: {query_5.title()} | Password: {query_6} \n')
      print( f" Password added.....Check this link '{passwd_path}'")
      query_7= input(' want to add again? type a to add and q to quit: ').lower()
      if query_7== 'a':
        return add_passwd()
      elif query_7== 'q':
        quit()
      else:
        return ' learn to follow instructions!! '  
    else:
      file.write(f'Username/Account: none | password: {query_6} \n')
      print( f" Password added.. Check this link '{passwd_path}'")
      query_7= input(' want to add again? type a to add and q to quit. ').lower()
      if query_7== 'a':
        return add_passwd()
      elif query_7== 'q':
        quit()
      else:
        return 'Learn to follow instructions!! '     


print(input_checker(query))
 