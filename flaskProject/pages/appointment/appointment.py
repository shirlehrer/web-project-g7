from flask import Blueprint, render_template, redirect, url_for, request, flash,session
from flaskProject.utilities.db.contact_queries import ContactManager

# about blueprint definition
appointment = Blueprint('appointment', __name__, static_folder='static', static_url_path='/appointment', template_folder='templates')


# Routes
@appointment.route('/appointment', methods=['GET', 'POST'])
def index():
    #complete_comment = False
    if request.method == 'POST':
        full_name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        date = request.form['date']
        description = request.form['description']
        ContactManager.addAppointment(full_name, phone, email, description, date)
        #complete_comment = True
        flash('Tnx for contacting us we will contact you back as soon as possible')
        return redirect(url_for('homepage.index'))
    return render_template('appointment.html')