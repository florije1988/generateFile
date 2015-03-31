# -*- coding: utf-8 -*-
import os
import datetime
from flask import __version__ as version

# PROJECT
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=12)
STATIC_PATH = 'static'
FLASK_SECRET_KEY = 'generat0rap1'

# LOGGING
LOG_FILE = './log/app.log'
LOG_LEVEL = 'DEBUG'
LOG_SIZE = 100000000

# Files configuration
EXTENSION = '.docx'
REPOSITORY = '/static/files/'
