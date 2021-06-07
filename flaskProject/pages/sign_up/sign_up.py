from flask import Blueprint, render_template

# gallery blueprint definition
catalog = Blueprint('sign_up', __name__, static_folder='css', static_url_path='/sign_up', template_folder='templates')


# Routes
@catalog.route('/sign_up')
def index():
    return render_template('sign_up.html')
