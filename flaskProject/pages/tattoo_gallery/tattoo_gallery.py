from flask import Blueprint, render_template

# gallery blueprint definition
tattoo_gallery = Blueprint('tattoo_gallery', __name__, static_folder='static', static_url_path='/tattoo_gallery', template_folder='templates')


# Routes
@tattoo_gallery.route('/tattoo_gallery')
def index():
    return render_template('tattoo_gallery.html')

