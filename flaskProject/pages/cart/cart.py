from flask import Blueprint, render_template

# about blueprint definition
about = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')


# Routes
@about.route('/cart')
def cart():
    return render_template('cart.html')


