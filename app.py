from flask import Flask, make_response, request, session, render_template, jsonify
import jwt
from datetime import datetime, timedelta
from functools import wraps

# instantiate flask class
app = Flask("__name__")
app.config['SECRET_KEY'] = 'ac5eaa702ff643e28cc2d2821b47c342'


@app.route('/')   
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    return 'Logged in!'

def token_required(func):
    @wraps(func)  # decorator factory to apply update_wrapper() to a wrapper function
    def decorated(*args,**kwargs):  # passing the positional and keywords arguments

        token = request.args.get('token')   #getting the token
        if not token:
            return jsonify({"Alert!": "Token is missing.."}),401
        try:
            # while decoding token, secret key & algorithms for hashing used should be passed
            payload = jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])
        except:
            # catches the exception when it cant decode 
            return jsonify({"Alert!": "Token is invalid"}),401
        return func(*args,**kwargs)

    return decorated

# public
@app.route('/public')
def public():
    return jsonify({"message":'This is for the public'})

# Authorized
@app.route("/auth")
@token_required
def auth():
    return jsonify({"message": 'This is for the authorized, Token is validated'})


# login
@app.route('/login',methods=["POST"])
def login():
    user_name = request.form['username']
    password = request.form['password']
    # auth = request.authorization is used instead of creating a seperate html 
    if user_name and password == '123456':
        session['logged_in'] = True
        # token encoded with the username to identify user , exp is the keyword for the expiration time
        token = jwt.encode( 
            {'username' : user_name, 'exp' : datetime.now() + timedelta(minutes=10)},
            app.config['SECRET_KEY'])
        return jsonify({'token' : token})
    else:
        # WWW-Authenticate ->  response header defines the HTTP authentication methods
        return make_response( 'Unable to verify', 401, {'WWW-Authenticate' : 'Basic realm="Authentication Failed!"'})



if __name__ == "__main__":
    app.run(debug=True)
