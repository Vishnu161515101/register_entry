# code
# Import all important libraries
from flask import *
import pymysql
import re
from flask import request
from flask import render_template
from flask import Flask
from flask import redirect

# initialize first flask
app = Flask(__name__)
app.secret_key = 'xyzsdfg'

# Create a single time database connection object
db_mysql = pymysql.connect(host='localhost', user='root', password='', db='vishnu')

# Create a cursor object from the connection
db_cursor = db_mysql.cursor()



# Make login function for login and also make 
# session for login and registration system 
# and also fetch the data from MySQL

@app.route('/')
@app.route('/login' ,methods=['GET', 'POST'])
def login():
		message = ''
		if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
				email = request.form['email']
				password = request.form['password']
				sql1="select * from login where email_id='{}' and password='{}'".format(email,password)
				db_cursor.execute(sql1)
				data=db_cursor.fetchall()
				if data:
					message = 'Logged in successfully !'
					return render_template('admin.html', message=message)
				else:
					message = 'Please enter correct email / password !'
					# return 'hello vishnu it is succesfull'
				# return render_template('login.html', message=message)
		return render_template('login.html', message=message)
	
	

@app.route('/Register', methods=['GET', 'POST'])
def Register():
	message = ''
	if request.method == 'POST' and 'name' in request.form and 'password' in request.form and'email' in request.form:
			userName = request.form['name']
			password = request.form['password']
			email = request.form['email']
			sql1="select * from login where email_id='{}' and password='{}'".format(email,password)
			db_cursor.execute(sql1)
			data=db_cursor.fetchall()
			if data:
				message = 'Account already exists !'
				# return 'helo'
			elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
				message = 'Invalid email address !'
				# return 'helo'
			elif not userName or not password or not email:
				message = 'Please fill out the form !'
				# return 'helo'
			else:
				sql="insert into login(name,password,email_id)values('{}','{}','{}')".format(userName,password,email)
				db_cursor.execute(sql)
				db_mysql.commit()
				message = 'You have successfully registered !'
				# return 'hello vishnu this register page'
			# return 'hello'
	elif request.method == 'POST':
		message = 'Please fill out the form !'
		# return render_template('register.html', message=message)
	return render_template('Register.html', message=message)

@app.route('/logout')
def logout():
    # session.pop('loggedin', None)
    # session.pop('userid', None)
    # session.pop('email', None)
    return redirect(url_for('login'))


# run code in debug mode
if __name__ == "__main__":
	app.run(debug=True)
