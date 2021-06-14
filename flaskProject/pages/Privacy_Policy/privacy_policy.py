from flask import Blueprint, render_template

# gallery blueprint definition
catalog = Blueprint('privacy_policy', __name__, static_folder='css', static_url_path='/privacy_policy', template_folder='templates')


# Routes
@catalog.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')
