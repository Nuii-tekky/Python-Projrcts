import json
from difflib import get_close_matches


# calling the dictionary from the json file and opening it
dictionary= json.load(open('Python_Apps\Dictionary _ Json\data.json'))
user_word= input('enter a word: ')

# now i get the user input and check for spelling error
def get(user_input):

  user_input=user_input.lower()
  

  if user_input in dictionary:
    return dictionary[user_input]

  elif len(get_close_matches(user_input,dictionary.keys()))>0:
    yes_no= input('did you mean %s? If yes type \'y\' or no type \'n\': ' % get_close_matches(user_input,dictionary.keys()) [0])
    if yes_no== 'y':
      return dictionary[get_close_matches(user_input,dictionary.keys()) [0]]
    elif yes_no=='n':
      return 'word not found,please review your spellings'  
    else:
      return 'you are a confused person'
      
  else: 
    return 'the word you entered does not exist or is incorrectly spelt'
  

# now lets store the output in a variable so we can perform actions with it

output= get(user_word)
# we want to display output in seperate lines in a list     
if type(output) == list:
  for item in output: print(item)
else:
  print(output)    