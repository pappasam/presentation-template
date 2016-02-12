import os

basedir = os.path.dirname(os.path.abspath(__file__))

class ConfigBase(object):
    SECRET_KEY = 'myhardstring'

    @staticmethod
    def init_app(app):
        pass


class ConfigDevelopment(ConfigBase):
    DEBUG = True

class ConfigProduction(ConfigBase):
    DEBUG = False

config = {
        'base': ConfigBase,
        'development': ConfigDevelopment,
        'production': ConfigProduction,
        'default': ConfigDevelopment,
        }
