from flask import Blueprint, render_template, redirect, url_for

# gallery blueprint definition
privacy_policy = Blueprint('privacy_policy', __name__, static_folder='static', static_url_path='/privacy_policy', template_folder='templates')

# Routes
@privacy_policy.route('/')
def index():
    return render_template('privacy_policy.html')

@privacy_policy.route('/privacy_policy')
@privacy_policy.route('/privacy_policy_page')
def redirect_privacy_policy():
    return redirect(url_for('privacy_policy.index'))

