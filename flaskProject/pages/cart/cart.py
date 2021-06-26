import datetime

from flask import Blueprint, render_template, redirect, url_for, session , request, flash

# about blueprint definition
from flaskProject.utilities.db.contact_queries import ContactManager
from flaskProject.utilities.db.shop_queries import ShopManager
from flaskProject.utilities.db.user_queries import UserManager

cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')

# Routes
@cart.route('/cart')
def index():
    logged = False
    Cartmassage = True
    if 'logged_in' in session:
        logged = True
        user_name = session['user_name']
        cart_products = ShopManager.getCart(user_name)
        if len(cart_products) > 0:
            Cartmassage = False
        return render_template('cart.html', cart_products=cart_products, logged=logged, Cartmassage=Cartmassage)
    else:
        return render_template('cart.html', logged=logged, Cartmassage=Cartmassage)

@cart.route('/cart/addOrder/<user_name>', methods=['GET', 'POST'])
def addOrder(user_name):
    dateTime = datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    cvv = request.form['cvv']
    cc = request.form['cc']
    user_email = UserManager.getUserEmail(user_name)
    user_first_name = UserManager.getUserFirstName(user_name)
    user_last_name = UserManager.getUserLastName(user_name)
    order_id = ShopManager.createNewOrder(user_name, user_first_name, user_last_name, user_email, cc, cvv)
    ShopManager.moveFromCartToOrder(user_name,order_id)
    ShopManager.deleteCart(user_name)
    return redirect(url_for('cart.index'))

@cart.route('/deleteProduct/<p_name>/<user_name>', methods=['GET', 'POST'])
def deleteProduct(p_name, user_name):
    ShopManager.removeProductsFromCart(p_name, user_name)
    return redirect(url_for('cart.index'))
