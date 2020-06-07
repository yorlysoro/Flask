from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

with app.test_request_context('/hello', method='POST'):
	assert request.path == '/hello'
	assert request.method == 'POST'