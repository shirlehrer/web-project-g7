from flask import Blueprint, render_template

# gallery blueprint definition
catalog = Blueprint('treatment', __name__, static_folder='css', static_url_path='/treatment', template_folder='templates')


# Routes
@catalog.route('/treatment')
def index():
    return render_template('treatment.html')
