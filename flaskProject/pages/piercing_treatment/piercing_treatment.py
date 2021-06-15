from flask import Blueprint, render_template

# gallery blueprint definition
piercing_treatment = Blueprint('piercing_treatment', __name__, static_folder='static', static_url_path='/piercing_treatment', template_folder='templates')


# Routes
@piercing_treatment.route('/piercing_treatment')
def index():
    return render_template('piercing_treatment.html')


