##############################################
# This example we add "about" page
# check result in: http://127.0.0.1:5000/about
##############################################

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	# return "hello world!"
	return "<h1>hello world!</h1>"

@app.route("/about")
def about():
	return "<h1>About Page</h1>"


if __name__ == '__main__':
	app.run(debug=True)