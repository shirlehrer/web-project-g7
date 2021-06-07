from flask import Blueprint, render_template

# gallery blueprint definition
catalog = Blueprint('tattoo_treatment', __name__, static_folder='css', static_url_path='/tattoo_treatment', template_folder='templates')


# Routes
@catalog.route('/tattoo_treatment')
def index():
    return render_template('tattoo_treatment.html')
