from flask import Blueprint, render_template

# gallery blueprint definition
tattoo_treatment = Blueprint('tattoo_treatment', __name__, static_folder='static', static_url_path='/tattoo_treatment', template_folder='templates')


# Routes
@tattoo_treatment.route('/tattoo_treatment')
def index():
    return render_template('tattoo_treatment.html')

