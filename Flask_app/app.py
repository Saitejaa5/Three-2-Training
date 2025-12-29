from flask import Flask, render_template, request
from models import init_db, add_user, check_user

app = Flask(__name__)
app.secret_key = "secret_key"

init_db()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if add_user(username, password):
            return render_template('index.html', message="User registered successfully")
        else:
            return render_template('index.html', message="invalid details")

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if check_user(username, password):
            return render_template('index.html', message="Login successful")
        else:
            return render_template('login.html', message="Invalid credentials")

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)