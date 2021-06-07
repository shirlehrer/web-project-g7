from flask import Blueprint, session

# main_menu blueprint definition
footer = Blueprint('header', __name__, static_folder='static', static_url_path='/header', template_folder='templates')

