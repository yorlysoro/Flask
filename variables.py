from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profilename(username):
	return 'User %s' % format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return 'Subpath %s' % format(subpath)

@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about/')
def about():
	return 'The about page'