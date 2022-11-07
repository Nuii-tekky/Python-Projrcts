
import time
from datetime import datetime as dtm

path= 'C:\Windows\System32\drivers\etc\hosts'

redirect= '127.0.0.1'
websites= ['www.youtube.com ',' youtube.com',' www.facebook.com',' facebook.com','kimoitv.com','www.kimoitv.com']

while True:
  if dtm(dtm.now().year,dtm.now().month,dtm.now().day,8) < dtm.now() < dtm(dtm.now().year,dtm.now().month,dtm.now().day,16):
    with open(path,'r+') as file:
      content= file.read()
      for website in websites:
        if website in content:
          pass 
        else:
          file.write(redirect+" "+ website + "\n")
    print('Working/coding hours... ')      
  else:
    with open(path,'r+') as file:
      content= file.readlines()
      file.seek(0)
      for line in content:
        if not any(website in line for website in websites):
          file.write(line)
        file.truncate()
    print('Fun Hours.... ')
    
  time.sleep(6)

 # the file.readlines() is to make the hosts file into a list that we can iterate through
 # the file.seek(0) is to place the pointer at the beginning of the hosts file to iterate and write to
 # then file.truncate() deletes all content below the pointer


    