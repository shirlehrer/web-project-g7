from flask import Blueprint, session, render_template, request, flash, redirect, url_for
from flaskProject.utilities.db.user_queries import UserManager

# main_menu blueprint definition
header = Blueprint('header', __name__, static_folder='static', static_url_path='/header', template_folder='templates')


@header.route('/header', methods=['GET', 'POST'])
def index():
    return render_template('homepage.html')


@header.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect('/homepage')

@header.route('/personal_page_check')
def pp_check():
    if not session['logged_in']:
        flash('Sorry, you need to be a member :( you can join us through SIGN UP')
        return redirect(url_for('homepage.index'))
    return redirect(url_for('personal_page.index'))



