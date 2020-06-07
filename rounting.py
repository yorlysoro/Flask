from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_page():
	return 'Index Page'

@app.route('/hello')
def hello_world():
	return 'Hello World'