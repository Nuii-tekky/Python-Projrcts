
from flask import render_template,request,Flask

webpage= Flask(__name__)

# render home page
@webpage.route("/")
def render_landing_page():
    return render_template('sample.html')  

# render success page
@webpage.route("/success.html",methods= ['post'])
def render_success_page():
    first_name= request.form['firstname']
    last_name= request.form['lastname']
    email= request.form['email']
    telephone= request.form['telephone']
    print(first_name.title(),last_name.title(),email,int(telephone))
    return render_template('success.html')


if __name__== '__main__':
  webpage.debug= True
  webpage.run()