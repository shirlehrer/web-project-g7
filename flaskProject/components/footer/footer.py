from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from flaskProject.utilities.db.contact_queries import ContactManager

# main_menu blueprint definition
footer = Blueprint('footer', __name__, static_folder='static', static_url_path='/footer', template_folder='templates')


@footer.route('/footer', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        massage = request.form['massage']
        ContactManager.addContactReq(first_name, last_name, email, massage)
        flash('Tnx for contacting us!')
        return redirect(url_for('homepage.index'))
    return redirect(url_for('homepage.index'))

