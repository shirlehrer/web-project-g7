from flask import Blueprint, render_template

# gallery blueprint definition
piercing_gallery = Blueprint('piercing_gallery', __name__, static_folder='static', static_url_path='/piercing_gallery', template_folder='templates')


# Routes
@piercing_gallery.route('/piercing_gallery')
def index():
    return render_template('piercing_gallery.html')


