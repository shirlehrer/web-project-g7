from flask import Blueprint, render_template, redirect, url_for

# about blueprint definition
cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')


# Routes
@cart.route('/cart')
def index():
    return render_template('cart.html')




