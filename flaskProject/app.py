from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from flaskProject.pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from flaskProject.pages.about.about import about
app.register_blueprint(about)

## Cart
from flaskProject.pages.cart.cart import cart
app.register_blueprint(cart)

## Privacy Policy
from flaskProject.pages.Privacy_Policy.privacy_policy import privacy_policy
app.register_blueprint(privacy_policy)

## Shop
from flaskProject.pages.shop.shop import shop
app.register_blueprint(shop)

## Signup
from flaskProject.pages.sign_up.sign_up import sign_up
app.register_blueprint(sign_up)

## Gallery
from flaskProject.pages.gallery.gallery import gallery
app.register_blueprint(gallery)

## Piercing Gallery
from flaskProject.pages.piercing_gallery.piercing_gallery import piercing_gallery
app.register_blueprint(piercing_gallery)

## Tattoo Gallery
from flaskProject.pages.tattoo_gallery.tattoo_gallery import tattoo_gallery
app.register_blueprint(tattoo_gallery)

## Treatment
from flaskProject.pages.treatment.treatment import treatment
app.register_blueprint(treatment)

## Tattoo Treatment
from flaskProject.pages.tattoo_treatment.tattoo_treatment import tattoo_treatment
app.register_blueprint(tattoo_treatment)

## Piercing Treatment
from flaskProject.pages.piercing_treatment.piercing_treatment import piercing_treatment
app.register_blueprint(piercing_treatment)

## Personal page
from flaskProject.pages.user_personal_page.personal_page import personal_page
app.register_blueprint(personal_page)

## Page error handlers
from flaskProject.pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from flaskProject.components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

## Header
from flaskProject.components.header.header import header
app.register_blueprint(header)

## Footer
from flaskProject.components.footer.footer import footer
app.register_blueprint(footer)