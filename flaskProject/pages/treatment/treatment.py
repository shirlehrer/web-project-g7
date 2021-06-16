from flask import Blueprint, render_template

# gallery blueprint definition
treatment = Blueprint('treatment', __name__, static_folder='static', static_url_path='/treatment', template_folder='templates')


# Routes
@treatment.route('/treatment')
def index():
    return render_template('treatments.html')

