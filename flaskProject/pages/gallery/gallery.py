from flask import Blueprint, render_template

# gallery blueprint definition
catalog = Blueprint('gallery', __name__, static_folder='css', static_url_path='/gallery', template_folder='templates')


# Routes
@catalog.route('/gallery')
def gallery():
    return render_template('Gallery.html')

