from flask import Blueprint, render_template

# gallery blueprint definition
piercing_gallery2 = Blueprint('piercing_gallery2', __name__, static_folder='static',
                              static_url_path='/piercing_gallery2', template_folder='templates')


# Routes
@piercing_gallery2.route('/piercing_gallery2')
def index():
    return render_template('piercing_gallery2.html')


