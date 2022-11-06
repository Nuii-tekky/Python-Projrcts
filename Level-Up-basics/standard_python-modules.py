

# standard python modules unlike the built ins are not gotten from the list gotten from sys.builtin_module_names

# it is much more powerful than the built in modules

# the key difference is that when you installed pyhton the standard python moduiles came as one of the installation files while the built in modules......  wtf? am i saying!!!!!
# all that matters is that i know what am talking about


import os
# you can check what methods this module offers
# dir(os)

os.path.exists('Level-Up-basics/note.txt')
# the os signifies the module,the path signifies the method and exists()signifies the object

# that piece of code checks if a file exists


if os.path.exists('Level-Up-basics/note.txt'):
  print('it worked')
else:
  print('This file or directory cannot be accessed right now')  