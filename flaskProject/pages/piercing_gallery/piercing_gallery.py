from flask import Blueprint, render_template

# gallery blueprint definition
catalog = Blueprint('piercing_gallery', __name__, static_folder='css', static_url_path='/piercing_gallery', template_folder='templates')


# Routes
@catalog.route('/piercing_gallery')
def piercing_gallery():
    return render_template('piercing_gallery.html')


