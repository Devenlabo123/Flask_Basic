from flask import Flask, render_template
from data import *

app = Flask(__name__)

Response=salesResponse()

@app.route('/')
def index():
    return render_template('home.html', response=Response)
     
if __name__ == '__main__':
    app.run(debug=True)