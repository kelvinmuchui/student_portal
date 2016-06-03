from flask import Flask, render_template ,request, redirect, url_for,session,flash


app = Flask(__name__)

app.secret_key = "my precious" 
  




                #index
# use decorators to link the function to a url
@app.route('/')
def home():
	#return "This is cool"# return a string
	return render_template("index.html")




            #welcome
@app.route('/welcome')
def welcome():
	return render_template("welcome.html") #return a template





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
# 	return render_template('login.html', error = error)



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
def logout():
	session.pop(' logged_in', None)
	flash('You were just logged out')
	return redirect(url_for('welcome'))




# start the server with the "run()" method
if __name__ == '__main__':
	app.run(debug=True)
