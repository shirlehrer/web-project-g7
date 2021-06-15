from flask import Blueprint, render_template

# gallery blueprint definition
sign_up = Blueprint('sign_up', __name__, static_folder='static', static_url_path='/sign_up', template_folder='templates')


# Routes
@sign_up.route('/sign_up')
def index():
    return render_template('sign_up.html')


