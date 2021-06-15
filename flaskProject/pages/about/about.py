from flask import Blueprint, render_template, redirect, url_for

# about blueprint definition
about = Blueprint('about', __name__, static_folder='static', static_url_path='/about', template_folder='templates')


# Routes
@about.route('/')
def index():
    return render_template('about.html')

@about.route('/about')
@about.route('/about_page')
def redirect_about():
    return redirect(url_for('about.index'))
