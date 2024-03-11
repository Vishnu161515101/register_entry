# code
# Import all important libraries
from flask import *
import pymysql
import re
from flask import request
from flask import render_template
from flask import Flask
from flask import redirect
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_mail import Mail, Message 
import random
app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jayaramireddy063@gmail.com'  # Replace with your email address
app.config['MAIL_PASSWORD'] = 'qwgh ulfg xtnl zgaf'  # Replace with your email password


mail = Mail(app)
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
				msg = Message("Hello",sender="jayaramireddy063@gmail.com",recipients=["vishnuvardhan12345@gmail.com"])
				mail.send(msg)
				
				message = 'You have successfully registered !'
				# return 'hello vishnu this register page'
			# return 'hello'
	elif request.method == 'POST':
		message = 'Please fill out the form !'
		# return render_template('register.html', message=message)
	return render_template('Register.html', message=message)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/test')
def test():
	return render_template('Register1234.html')
@app.route('/Register1234', methods=['POST'])
def Register1234():
    if request.method == 'POST':
        userName = request.form['userName']
        password = request.form['password']
        email = request.form['email']

        # Assuming you have already established a database connection and have a cursor
        # Performing database operations...
        
        sql = "insert into login(name,password,email_id) values('{}','{}','{}')".format(userName, password, email)
        db_cursor.execute(sql)
        db_mysql.commit()

        number = random.randint(1111, 9999)
        msg = Message(subject=message, sender='jayaramireddy063@gmail.com', recipients=[email])
        msg.body = f"{body}, {number}"  # Concatenate message body and random number
        mail.send(msg)
        return "Message sent!"

        message = 'You have successfully registered !'
        return message

# run code in debug mode
if __name__ == "__main__":
	app.run(debug=True)
