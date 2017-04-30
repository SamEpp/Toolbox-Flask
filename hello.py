"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'This is my Index Page: hi from sam'

# @app.route('/hello')
# def hello():
#     return 'Hello World'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
