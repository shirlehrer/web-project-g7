from flask import Blueprint, render_template, session, request, flash
from flaskProject.utilities.db.user_queries import UserManager
from flaskProject.utilities.db.contact_queries import ContactManager
from flaskProject.utilities.db.shop_queries import ShopManager

# gallery blueprint definition
personal_page = Blueprint('personal_page', __name__, static_folder='static', static_url_path='/personal_page',
                          template_folder='templates')


# Routes
@personal_page.route('/personal_page')
def index():
    logged = False
    Omassage = False
    Amassage = False
    if 'logged_in' in session:
        user_details = UserManager.getUser(session['email'])
        email = session['email']
        apps = ContactManager.getApps(email)
        if len(apps) == 0:
            Amassage = True
        order = ShopManager.getOrdersproducts(email)
        if len(order) == 0:
            Omassage = True
        logged = True
        return render_template('personal_page.html', account=user_details, apps=apps, logged=logged, order=order,
                               Omassage=Omassage, Amassage=Amassage)
    return render_template('personal_page.html', logged=logged)



@personal_page.route('/update_details', methods=['GET', 'POST'])
def update_details():
    if request.method == 'POST':
        email = session['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        user_name = request.form['user_name']
        password = request.form['password']
        update = UserManager.updateUser(first_name, last_name, user_name, password, email)
        user = UserManager.getUser(email)
        print(user)
        session['user_name'] = user[0].user_name
        session['last_name'] = user[0].last_name
        session['first_name'] = user[0].first_name
        #session['email'] = user[0].email
        session['password'] = user[0].password
        flash('User details were updated successfully')
    return render_template('/personal_page.html')


