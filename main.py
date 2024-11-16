from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

'''EL DETALLE ES QUE TIENEN QUE TENER EL MISMO TAMANO'''
productos = [
    {"id": 1, "nombre": "Trompo pastor con verduras", "precio": 15000.00, "imagen": "static/assets/img/trompo.jpeg"},
    {"id": 2, "nombre": "Pantalones Negros", "precio": 400.00, "imagen": "static/assets/img/shop_02.jpg"},
    {"id": 3, "nombre": "Zapatos Deportivos", "precio": 600.00, "imagen": "static/assets/img/shop_03.jpg"},
    {"id": 4, "nombre": "Bolsa Azul", "precio": 150.00, "imagen": "static/assets/img/shop_04.jpg"},
    {"id": 5, "nombre": "Gorra Negra", "precio": 50.00, "imagen": "static/assets/img/shop_05.jpg"},
    {"id": 6, "nombre": "Gorra Negra", "precio": 50.00, "imagen": "static/assets/img/shop_05.jpg"},
    {"id": 7, "nombre": "Gorra Negra", "precio": 50.00, "imagen": "static/assets/img/shop_05.jpg"},
    {"id": 8, "nombre": "Gorra Negra", "precio": 50.00, "imagen": "static/assets/img/shop_05.jpg"},
]


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    return render_template('shop.html', productos=productos)

@app.route('/contact')
def contact():
    return render_template('contact.html')

# @app.route('/shop-single/<int:product_id>')
# def shop_single(product_id):
#     producto = next((p for p in productos if p["id"] == product_id), None)
#     if producto is None:
#         return "Producto no encontrado", 404
#     return render_template('shop_single.html', producto=producto)


@app.route('/shop-single')
def shop_single():
    return render_template('shop_single.html')

if __name__ == '__main__':
    app.run(debug=True)
