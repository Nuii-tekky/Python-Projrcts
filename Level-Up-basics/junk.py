
import os
# def check_existence():
#   my_text= open('Level-Up-basics/demo.txt')
#   if os.path.exists('Level-Up-basics/demo.txt'):
#     return my_text.read()
#   else:
#     return 'File not found'

# print(check_existence())   

def write_to_file():
  if os.path.exists('Level-Up-basics/demo.txt'):
    with open('Level-Up-basics/demo.txt','r+') as file:
      contents= file.read()
    with open(r'C:\Users\ekomobong\Documents/sampleDropbox.txt','a') as sample:
      sample.write(contents) 
  else:
    print(' file not found')

write_to_file()      