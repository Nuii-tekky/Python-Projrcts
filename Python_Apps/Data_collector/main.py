from flask import render_template,request,Flask


webpage= Flask(__name__)


# render home page
@webpage.route("/")
def render_landing_page():
    return render_template('sample.html')  

@webpage.route("/success.html",methods= ['post'])
def render_success_page():
    email= request.form['email']
    print(email)
    return render_template('success.html')


if __name__== '__main__':
  webpage.debug= True
  webpage.run()


