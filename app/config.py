import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'somethingProfaneYouWillNeverGuess'
    ADMINS = frozenset(['youremail@yourdomain.com'])

    CSRF_ENABLED=True
    CSRF_SESSION_KEY="somethingimpossibletoguess"

    DEBUG = True
    TESTING = True
    _basedir = os.path.abspath(os.path.dirname(__file__))


    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
    #   DATABASE_CONNECT_OPTIONS = {}



