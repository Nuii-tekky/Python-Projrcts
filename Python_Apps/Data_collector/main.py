from flask import render_template,request,Flask

webpage= Flask(__name__)

# render home page
@webpage.route("/")
def render_landing_page():
  return render_template('sample.html')

# render success page
@webpage.route("/success",methods= ['POST'])
def render_success_page():
  if request.method== 'POST':
    email= request.form['email']
    print(f'your email is {email} ')
    return render_template('success.html')
  
if __name__== '__main__':
  webpage.debug= True
  webpage.run()
