# -*- coding: utf-8 -*-
###########################################
from flask import Flask
from flask import request

#####################################
# flash uses decorator to bind URL to functions
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return '''
    <h1>Home</h1>
    '''

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''
    <form action="/signin" method="post">
    <p><input name = "username"></p>
    <p><input name = "password" type = "password"></p>
    <p><button type = "submit">Sign In</button></p>
    '''


@app.route('/signin', methods=['POST'])
def signin():
    # need to read form content from request object
    if request.form['username'] == 'admin' and request.form['password']=='123':
        return '<h3>Welcome, admin!</h3>'
    return '<h3>Bad username or passord</h3>'

if __name__ == '__main__':
    app.run()

