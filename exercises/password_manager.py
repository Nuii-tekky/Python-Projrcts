import os

print('Welcome to the ultimate Password manager: ')

def action():
  query= input('Before we continue, type in the master password: ')
  query2= input('Do you wanna view or add passwords (v or a) or q to quit: ').lower()
  if query2== 'v':
    return view()
  elif query2== 'a':
    return add()
  elif query2== 'q':
    quit()  
  else:
    return 'invalid input! ' 


def add():
  user_name= input('enter the account username: ')
  passwd= input('enter the password: ')

  with open(r'C:\Users\ekomobong\Documents\My Projects\Python\Python-sandboxes\passwords.txt','a') as file:
    file.write(user_name+ "|" + passwd + '\n')

def view():
  path= r'C:\Users\ekomobong\Documents\My Projects\Python\Python-sandboxes\passwords.txt'

  with open(path,'r') as file:
    content= file.read()
  if os.path.getsize(path) == 0:
    query3= input('No passwords added.type a to add and q to quit: ')
    if query3== 'a':
      return add()
    elif query3== 'q':
      quit()
    else:
      return 'invalid input! ' 
  else:
    return content


print(action())          