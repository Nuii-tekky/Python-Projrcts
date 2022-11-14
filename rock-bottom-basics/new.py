import os
import sys


current_dir= r"C:\Users\ekomobong\Documents\My Projects\Python\Python-sandboxes\rock-bottom-basics"
new_file_path= r'C:\Users\ekomobong\Documents\My Projects\Python\Python-sandboxes\rock-bottom-basics\files.txt'

for files in os.listdir(current_dir):
  with open(new_file_path,'w+') as new_file:
    new_file.write(files)









































# user_input= input('enter a wrestler: ')

# message='%s is not a good wrestler' % user_input

# print(message)

# #--------------------------------------------------------------------------

# name= input('Please insert your first-name')
# surname= input('Please insert your last-name')
# hobby= input('Whats your hobby')
# status= input('is a dog an animal')
