import os
import sys


with open(r'C:\Users\ekomobong\Documents\My Projects\Python\Python-sandboxes\rock-bottom-basics\files.txt','w') as new_file:
  new_file.write(list)


list= []

current_dir= os.getcwd()
for files in os.listdir(current_dir):
  list.append(files)














































# user_input= input('enter a wrestler: ')

# message='%s is not a good wrestler' % user_input

# print(message)

# #--------------------------------------------------------------------------

# name= input('Please insert your first-name')
# surname= input('Please insert your last-name')
# hobby= input('Whats your hobby')
# status= input('is a dog an animal')
