import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config(object):

    # retrieve secrete key from environment variable or default
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-not-die'

    # retrieve database source from environment variable or default or file
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')

    # used to signal/notify the application when an object changes
    SQLALCHEMY_TRACK_MODIFICATION = False

