from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret_key_for_session'


# In-memory storage for user data (for demonstration purposes only)
users = {'user1': 'password1', 'user2': 'password2'}


@app.route('/')
def index():
    return 'Welcome to the home page!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', message='Invalid username or password')

    return render_template('login.html', message='')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Hello, {session["username"]}! This is the secured dashboard.'
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
