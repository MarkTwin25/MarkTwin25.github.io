from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

'''EL DETALLE ES QUE TIENEN QUE TENER EL MISMO TAMANO'''
productos = [
    {"id": 1, "nombre": "Trompo pastor con verduras", "precio": 15000.00, "imagen": "static/assets/img/trompo.jpeg"},
    {"id": 2, "nombre": "Churrasco c/hueso", "precio": 5000.00, "imagen": "static/assets/img/churrasco.jpg"},
    {"id": 3, "nombre": "Mariscada Surtida", "precio": 6000.00, "imagen": "static/assets/img/mariscadap.jpg"},
    {"id": 4, "nombre": "Quesos Gourmet", "precio": 11000.00, "imagen": "static/assets/img/quesosg.jpg"},
    {"id": 5, "nombre": "Jitomates Importados", "precio": 4500.00, "imagen": "static/assets/img/jitomatesp.jpg"},
    {"id": 6, "nombre": "Agujas de Res", "precio": 50.00, "imagen": "static/assets/img/agujasp.jpg"},
    {"id": 7, "nombre": "Calabazas Otoñales", "precio": 3800.00, "imagen": "static/assets/img/calabazasp.jpg"},
    {"id": 8, "nombre": "Costillas de cerdo marinadas", "precio": 9000.00, "imagen": "static/assets/img/costillas.jpg"},
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

'''
@app.route('/shop-single/<int:product_id>')
def shop_single(product_id):
    producto = next((p for p in productos if p["id"] == product_id), None)
    if producto is None:
        return "Producto no encontrado", 404
    return render_template('shop-single.html', producto=producto)
'''


@app.route('/shop-single')
def shop_single():
    return render_template('shop-single.html')


if __name__ == '__main__':
    app.run(debug=True)
