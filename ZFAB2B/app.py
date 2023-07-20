from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    adet = db.Column(db.Integer, nullable=False, default=0)
    kdv = db.Column(db.Float, nullable=False)
    

class ProductView(ModelView):
    column_labels = {
        'name': 'Ürün Adı',
        'price': 'Fiyat',
        'adet': 'Adet',
        'kdv': 'KDV',
    }

    form_columns = ['name', 'price', 'adet', 'kdv']
    column_searchable_list = ['name']
    column_filters = ['name', 'price', 'adet', 'kdv']

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ProductView(Product, db.session))

@app.route('/')
def index():
      return render_template('index.html', products=products)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Kullanıcı adı ve şifrenin kontrolü
    user = User.query.filter_by(username=username, password=password).first()

    if user:
        session['user_id'] = user.id
        if username == 'admin' and password == 'admin':
            return redirect('/admin')
        else:
            return redirect(url_for('home'))
    else:
        error = 'Geçersiz kullanıcı adı veya şifre!'
        return render_template('index.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/takip', methods=['GET', 'POST'])
def takip():
    if request.method == 'POST':
        tracking_number = request.form['tracking_number']

        response = {
            'tracking_number': tracking_number,
            'status': 'In Transit',
            'location': 'Depo A',
            'estimated_delivery': '2023-07-15'
        }

        return jsonify(response)

    return render_template('takip.html')

@app.route('/takip-sonucu')
def takip_sonucu():
    tracking_number = request.args.get('tracking_number')  # Takip numarasını al

    # Takip işlemlerini gerçekleştir ve sonuçları takip.html ile paylaş
    # Örneğin, sonuçları bir değişkende toplayıp takip.html'e gönderilebilir

    return render_template('takip.html', tracking_number=tracking_number)

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    products = Product.query.filter(Product.name.ilike(f'%{search_query}%')).all()

    return render_template('ara.html', products=products)

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    return render_template('home.html')

@app.route('/products', methods=['GET', 'POST'])
def products():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        search_query = request.form['search_query']
        products = Product.query.filter(Product.name.ilike(f'%{search_query}%')).all()
    else:
        products = Product.query.all()

    total_price = 0
    for product in products:
        total_price = total_price + (product.price * product.adet * (1 + product.kdv / 100))

    return render_template('products.html', products=products, total_price=total_price)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
