from flask import Flask, render_template, jsonify
import secrets
import string

app = Flask(__name__)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password')
def get_password():
    password = generate_password()
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
