

print('Welcome to the ultimate Password manager: ')
query= input('Before we continue, type in the master password: ')

def check_query(value):
  if value == True:
    return what_action()
  else:
    return 'Invalid input! ' 

def what_action():
  query2= input('Do you wanna view or add passwords (v or a) or q to quit ').lower()
  if query2== 'v':
    return view()
  elif query2== 'a':
    return add()
  else:
    return 'invalid input! ' 


def add():
  user_name= input('enter the account username: ')
  passwd= input('enter the password')

  with open('passwords.txt','a') as file:
    file.write(f'{user_name} | {passwd} \n')      