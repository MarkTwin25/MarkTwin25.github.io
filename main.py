from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/shop-single')
def shop_single():
    return render_template('shop-single.html')

if __name__ == '__main__':
    app.run(debug=True)