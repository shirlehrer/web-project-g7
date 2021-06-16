from flask import Blueprint, render_template, redirect, url_for

# about blueprint definition
appointment = Blueprint('appointment', __name__, static_folder='static', static_url_path='/appointment', template_folder='templates')


# Routes
@appointment.route('/appointment')
def index():
    return redirect(url_for('appointment.index'))
