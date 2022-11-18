import json
from difflib import get_close_matches as gcm


# calling the dictionary from the json file and opening it
dictionary= json.load(open('Python_Apps\Dictionary _ Json\data.json'))
user_word= input('enter a word: ').lower()

# now i get the user input and check for spelling error
def Input_processor(user_input):
  if user_input in dictionary:
    return dictionary[user_input]

  elif len(gcm(user_input,dictionary.keys()))>0:
    yes_no= input(f"did you mean {gcm(user_input,dictionary.keys())[0]}? Type 'y' for yes and 'n' for no ")
    if yes_no== 'y':
      return dictionary[gcm(user_input,dictionary.keys()) [0]]
    elif yes_no=='n':
      return 'Word not found '  
    else:
      return "Your'e a confused person"
      
  else: 
    return 'The word you entered does not exist or is incorrectly spelt'
  

# now lets store the output in a variable so we can perform actions with it

output= Input_processor(user_word)
# we want to display output in seperate lines in a list     
if type(output) == list:
  for item in output: print(item)
else:
  print(output)    