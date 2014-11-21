from flask import Flask
from flask import request
from flask import session, g, redirect, url_for, abort, render_template, flash
import sqlites


#configuration
DATEBASE = '/tmp/endgame.db'
USERNAME='admin'
PASSWORD='default'
DEBUG= True


#app = Flask(__name__)

#@app.route('/', methods=['GET', 'POST'])
#def home():
    #return '<h1>Game Over</h1>'

#@app.route('/signin', methods=['GET'])
#def signin_form():
    #return '''<form action='/signin' methon='post'>
              #<p><input name ='username'></p>
              #<p><input name ='password' type="password"></p>
              #<p><button type="submit">Sign In</button></p>
	      #</form>'''

#@app.route('/signin', methods=['POST'])
#def signin_form():
    #if request.form['username']=='admin' and request.form['password']=='password':
        #return '<h3>Hello, admin!</h>'
    #return '<h3>Bad username or password!</h3>'


if __name__=='__main__':
    app.run('0.0.0.0')


