from flask import render_template,request,Flask

webpage= Flask(__name__)

# render home page
@webpage.route("/")
def render_landing_page():
  email= request.form['email']
  print(f'your email is {email} ')
  return render_template('sample.html')

  
if __name__== '__main__':
  webpage.debug= True
  webpage.run()
