# JWT
+ JWT -> Json Web Token
  + ## Traditional approach
    + Stores the user information (session)
    + Sends back the Session-Id
    + Session-Id is stored in the form of cookies as key-value pairs
    + Stateful-Protocol -> Saves the information at the backend
    + Less secure as the user is already authorized by the server
    + Authorization managed by the server side
  + ## JWT approach
    + No session information is stored at the backend
    + A private key (JWT) is initialized and given back to client side
    + Token is stored in the web local storage & is passed with the header
    + It is validated  by the server with the signature(SECRET_KEY)
+ JWT-WEBSITE -> `www.jwt.io`
## Imports
+ make_response -> to make the response
+ request -> to receive the response
+ render_template -> to generate a output form 
+ jsonify -> to convert the data into json  
+ wraps
  + wraps() is a decorator that is applied to the wrapper function of a decorator.
  + A decorator is a function that takes in another function as a parameter and then returns a function
  + Decorators provide a simple syntax for calling higher-order functions
## Secret Key
  + Generating secret keys
  + ```py
    import os
    print(os.urandom(12))
    >> b'3\x94\\\xa7NkN\xa2\xbc\x88\x11\x07'
    ```
  + ```py
    import uuid
    print(uuid.uuid4().hex)
    >> ac5eaa702ff643e28cc2d2821b47c342
    ```
  + ```py
    import secrets
    print(secrets.token_urlsafe(12))
    >> O-sMS8yAgxWAMTIG
    ```


## Run server
  + ```py
    python app.py
    ```

## Outputs
  + ## home
    + 
    ```
        URL: 127.0.0.1:5000/

        OP: Input form if not logged in already else input form
    ```
  + ## public
    + 
    ```
        URL: 127.0.0.1:5000/public

        OP:
            {
              "message": "This is for the public"
            }

        Remark: Always available as its a public url 
    ```
  + ## auth
    + Token missing
    ```
        URL: 127.0.0.1:5000/auth

        OP:
            {
              "Alert!": "Token is missing.."
            }

        Remark: Token is not included in the header
    ```
    + Invalid token
    ```
        URL: 127.0.0.1:5000/auth?token=abcd

        OP:
            {
              "Alert!": "Token is invalid"
            }

        Remark: Token is included in the header but not a valid one
    ```
    + Valid token
    ```
        URL: 127.0.0.1:5000/auth?token={some real token}

        OP:
            {
              "message": "This is for the authorized, Token is validated"
            }

        Remark: Token is included in the header and a valid one
    ```