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

## Catalog
from flaskProject.pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Page error handlers
from flaskProject.pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from flaskProject.components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)
