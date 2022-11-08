
from flask import Flask

website= Flask(__name__)
@website.route('/')

def index():
  return 'My Succesful web content'

if __name__== '__main__':
  website.run(debug=True)