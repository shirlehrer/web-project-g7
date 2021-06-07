from flask import Blueprint, render_template

# gallery blueprint definition
catalog = Blueprint('shop', __name__, static_folder='css', static_url_path='/shop', template_folder='templates')


# Routes
@catalog.route('/shop')
def index():
    return render_template('Shop.html')
