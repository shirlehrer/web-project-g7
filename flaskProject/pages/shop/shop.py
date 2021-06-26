from flask import Blueprint, render_template, session, flash, request

from flaskProject.utilities.db import shop_queries
from flaskProject.utilities.db.db_manager import dbManager
from flaskProject.utilities.db.user_queries import UserManager
from flaskProject.utilities.db.shop_queries import ShopManager
from datetime import datetime

# gallery blueprint definition
shop = Blueprint('shop', __name__, static_folder='static', static_url_path='/shop', template_folder='templates')


# Routes
@shop.route('/shop')
def index():
    return render_template('Shop.html')

# def products():
#     if 'logged_in' not in session:
#         flash('Hi guest, you need to be registered before ordering')
#         return render_template('Shop.html')
#     else:
#         cart = ShopManager.checkCartExists(session['email'])
#         if not cart:
#             ShopManager.createNewCart(session['user_name'], datetime=datetime.now())
#
#             order_id = ShopManager.insertProductsToOrders()


@shop.route('/add_product_to_cart/<p_name>/<user_name>', methods=['GET', 'POST'])
def add_product_to_cart(p_name, user_name):
    if request.method == 'POST':
        if session['logged_in']:
            AlreadyIn = ShopManager.checkProductInCart(p_name, user_name)
            quantity = request.form['quantity']
            if AlreadyIn:
                ShopManager.updateProductQuantity(p_name, user_name, quantity)
                flash("the product was already in your cart, we updated the quantity")
                return render_template('Shop.html')
            else:
                ShopManager.insertCart(p_name, user_name, quantity)
                flash("the product successfully added to your cart")
                return render_template('Shop.html')
        else:
            flash("you must sign in to add product to your cart")
            return render_template('Shop.html')





