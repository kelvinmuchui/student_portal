from flask import Flask, render_template ,request, redirect, url_for,session,flash
from functools  import wraps

app = Flask(__name__)

app.secret_key = "my precious" 
  
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap



                 #index
# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
 	#return "This is cool"# return a string
 	return render_template("index.html")




             #welcome
@app.route('/welcome')
def welcome():
 	return render_template("welcome.html") #return a templatu
 
 # @app.route('/login',  methods =['GET', 'POST'])
 # def login():
 # 	error = None
  # 	if request.form == 'POST':
 # 		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
 # 			error = 'invalid. please try again'

 # 		else:
 # 			session ['logged_in'] = True
 # 			flash('You were just logged in')
 # 			return redirect(url_for('home'))
	return render_template('login.html', error = error)



                    #login 
 # route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
         	session ['logged_in'] = True
 	        flash('You were just logged in')
 	        return redirect(url_for('home'))
    return render_template('login.html', error=error)


                #logout 
@app.route('/logout')
@login_required
def logout():
 	session.pop(' logged_in', None)
 	flash('You were just logged out')
 	return redirect(url_for('welcome'))




# # start the server with the "run()" method
if __name__ == '__main__':
 	app.run(debug=True)



# #from flask import Flask, render_template, redirect, url_for, request
# from flask import Flask, render_template, redirect, url_for, request, session, flash
# from functools import wraps
 
#  # create the application object
# app = Flask(__name__)
 
# # config
# app.secret_key = 'my precious'

# # login required decorator

# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('You need to login first.')
#             return redirect(url_for('login'))
#     return wrap

#  # use decorators to link the function to a url
# @app.route('/')
# @login_required
# def home():
#     return render_template('index.html')  # render a template
#     # return "Hello, World!"  # return a string
 
# @app.route('/login')
# def welcome():
#     def login():
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             session['logged_in'] = True
#             flash('You were logged in.')
#             return redirect(url_for('home'))
#     return render_template('index.html', error=error)
 
# @app.route('/logout')
# @login_required
# def logout():
#     session.pop('logged_in', None)
#     flash('You were logged out.')
#     return redirect(url_for('welcome'))

 
#  # start the server with the 'run()' method
# if __name__ == '__main__':
#     app.run(debug=True)
