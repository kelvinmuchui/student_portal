from flask import Flask, render_template ,request, redirect, url_for,session

app = Flask(__name__)

app.secret_key = "my precious" 

# use decorators to link the function to a url
@app.route('/')
def home():
	return "This is cool"# return a string

@app.route('/welcome')
def welcome():
	return render_template("welcome.html") #return a template

@app.route('/login',  methods =['GET', 'POST'])
def login():
	error = None
	if request.form == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'invalid. please try again'

		else:
			session ['logged_in'] = True
			return redirect(url_for('home'))
	return render_template('login.html', error = error)

@app.route('/logout')
def logout():
	session.pop(' logged_in', None)
	return redirect(url_for('welcome'))




# start the server with the "run()" method
if __name__ == '__main__':
	app.run(debug=True)
