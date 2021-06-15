from flask import Blueprint, render_template

# gallery blueprint definition
personal_page = Blueprint('personal_page', __name__, static_folder='static', static_url_path='/personal_page', template_folder='templates')


# Routes
@personal_page.route('/personal_page')
def index():
    return render_template('personal_page.html')

