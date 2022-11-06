#modules in python are very cool
#but like most things in python this not that explainable
# just remember that a module is a kind of library
#we have to use the import method to get a module in our script
#to see the list of built-in modules in python we use following syntax:

#sys.builtin_module_names

import time

# #we can use a feature of the sleep module to our convenience

while True:
    print('hello wrld')
    time.sleep(3)


# we can also use it with our "with loops"

while True:
    with open('Level-Up-basics/note.txt') as a_file:
        content= a_file.read()

    print(content)      


