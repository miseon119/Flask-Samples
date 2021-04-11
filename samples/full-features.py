from flask import Flask, render_template
app = Flask(__name__)

posts = [
	{
		'author': 'Wendy',
		'title': 'blog post1',
		'content': '1st post content',
		'date': 'May 1, 2020'
	},
	{
		'author': 'Bob',
		'title': 'blog post2',
		'content': '2nd post content',
		'date': 'May 2, 2020'
	},
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title="About")

if __name__ == '__main__':
	app.run(debug=True)