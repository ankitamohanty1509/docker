from flask import Flask 

app = Flask(__name__)
@app.route('/')
def hello_world():
   return 'Hello,world!'

if __name__ == '_main_':
    app.run(debug=True) 

