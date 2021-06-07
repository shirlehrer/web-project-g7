from flask import Blueprint, render_template

# gallery blueprint definition
catalog = Blueprint('piercing_treatment', __name__, static_folder='css', static_url_path='/piercing_treatment', template_folder='templates')


# Routes
@catalog.route('/piercing_treatment')
def index():
    return render_template('piercing_treatment.html')
