from flask import Blueprint, session, render_template

# main_menu blueprint definition
header = Blueprint('header', __name__, static_folder='static', static_url_path='/header', template_folder='templates')


@header.route('/header')
def index():
    return render_template('header.html')
