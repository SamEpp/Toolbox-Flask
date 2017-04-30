"""
This is my flask code that makes my website, the "result page", and the "not enough information page"
"""
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def hello_world():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
   error = None
   if request.method == 'POST':
      if request.form["Name"] and request.form["Age"] and request.form["Who is your favorite SoftDes Ninja"]:
        error = None
        return render_template("result.html", Name = request.form["Name"], Age = request.form["Age"])
      else:
       error = 'Please Fill In Fields'
       return render_template('neip.html')

if __name__ == '__main__':
    app.run()
