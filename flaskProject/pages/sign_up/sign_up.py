from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from flaskProject.utilities.db.user_queries import UserManager

# gallery blueprint definition
sign_up = Blueprint('sign_up', __name__, static_folder='static', static_url_path='/sign_up', template_folder='templates')


# Routes
@sign_up.route('/sign_up', methods=['GET', 'POST'])
def index():
    session['logged_in'] = False
    session['user_name'] = ''
    session['email'] = ''
    session['password'] = ''
    session['first_name'] = ''
    session['last_name'] = ''
    if request.method == 'POST':
        if 'first_name' in request.form:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            user_name = request.form['user_name']
            password = request.form['password']
            user_already_exist = UserManager.checkIfUserExists(email)
            if user_name == '' or first_name == '' or last_name == '' or email == '' or password == '':
                flash('PLEASE FILL ALL FIELDS!')
                return redirect('/sign_up')
            elif user_already_exist:
                flash('Hi! User already exists in the system')
                return render_template('sign_up.html')
            else:
                UserManager.insertNewUser(first_name, last_name, user_name, email, password)
                session['user_name'] = user_name
                session['email'] = email
                session['first_name'] = first_name
                session['last_name'] = last_name
                session['logged_in'] = True
                return redirect(url_for('homepage.index'))
    return render_template('sign_up.html')






