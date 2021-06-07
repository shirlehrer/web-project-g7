from flask import Blueprint, render_template

# gallery blueprint definition
catalog = Blueprint('personal_page', __name__, static_folder='css', static_url_path='/personal_page', template_folder='templates')


# Routes
@catalog.route('/personal_page')
def index():
    return render_template('personal_page.html')
