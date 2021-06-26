from flask import Blueprint, render_template, request, flash, redirect, session
from flaskProject.utilities.db.user_queries import UserManager

# gallery blueprint definition
sign_in = Blueprint('sign_in', __name__, static_folder='static', static_url_path='/sign_in', template_folder='templates')


# Routes
@sign_in.route('/sign_in', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['user_name'] = ''
        session['email'] = ''
        session['password'] = ''
        session['first_name'] = ''
        session['last_name'] = ''
        session['logged_in'] = False
        email = request.form['email']
        password = request.form['password']
        query = UserManager.getUserbyEmail(email)
        if len(query[0].user_name) == 0:
            flash('User does not exists, please sign up to our website')
            session['logged_in'] = False
            return render_template('homepage.html', logged_in=session['logged_in'])
        elif query[0].password != password:
            flash('username or password is incorrect, please try again')
            session['logged_in'] = False
            return render_template('sign_in.html')
        else:
            session['user_name'] = query[0].user_name
            session['email'] = email
            session['password'] = password
            session['first_name'] = query[0].first_name
            session['last_name'] = query[0].last_name
            session['logged_in'] = True
            return render_template('homepage.html', user_name=session['user_name'], logged_in=session['logged_in'])
    return render_template('sign_in.html')





