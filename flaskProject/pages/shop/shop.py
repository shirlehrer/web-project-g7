from flask import Blueprint, render_template, session, flash
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




