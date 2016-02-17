from flask import Flask
from config import config

class CustomFlask(Flask):
    '''Change the Jinja2 variable identifiers to %%
    Necessary because remarkjs uses handlebars for its
    template variable rendering, so {{ and }} are taken
    '''
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',
        variable_end_string='%%',
    ))

def create_app(config_name):
    app = CustomFlask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .views import views
    for view in views:
        app.register_blueprint(view)

    return app
