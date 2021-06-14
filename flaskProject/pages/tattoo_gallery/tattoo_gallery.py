from flask import Blueprint, render_template

# gallery blueprint definition
catalog = Blueprint('tattoo_gallery', __name__, static_folder='css', static_url_path='/tattoo_gallery', template_folder='templates')


# Routes
@catalog.route('/tattoo_gallery')
def tattoo_gallery():
    return render_template('tattoo_gallery.html')

