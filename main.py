from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dica():
    return render_template('demo-startup-agency.html')

@app.route('/login')
def login():
    return render_template('shop-login.html')


if __name__ == "__main__":
    app.run(debug=True)