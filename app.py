from flask import Flask, render_template
from data import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        result = request.form
        config = getConfig(result)
        capture = processCapture(result, config)
        auth = processAuth(result, config)
        return render_template('home.html', capture=capture, auth=auth)
    else:
        return render_template('home.html')
     
if __name__ == '__main__':
    app.run(debug=True)