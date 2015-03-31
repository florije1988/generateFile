#!flask/bin/python
# -*- coding: utf-8 -*-
from app import app, cfg
app.secret_key = cfg['FLASK_SECRET_KEY']
app.run(port=6621, debug=True)
