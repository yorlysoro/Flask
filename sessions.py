from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

app.secret_key = b'\x95\x10\x8d\xdeU\xce\x98\x13\xe4%\xb8bT\x82\x01\xca'

@app.route('/')
def index():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))