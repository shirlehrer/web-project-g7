from flask import Blueprint, session, render_template

# main_menu blueprint definition
footer = Blueprint('header', __name__, static_folder='static', static_url_path='/header', template_folder='templates')


def header():
    return None
@header.route('/header')
def header():
    return render_template('header.html')
