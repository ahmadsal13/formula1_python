from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the homepage'

if _name_ == "_main_":
    app.run(debug=True)