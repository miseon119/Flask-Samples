from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	# return "hello world!"
	return "<h1>hello world!</h1>"

if __name__ == '__main__':
	app.run(debug=True)