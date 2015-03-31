# -*- coding: utf-8 -*-
from flask import Flask, g, redirect, abort, make_response
import base64, config, datetime, gzip, hashlib, ldap, logging, os
from flask.ext.triangle import Triangle

app = Flask(__name__)

app.config.from_object('config')
cfg = app.config

format_string = "%(levelname) -10s %(asctime)s %(module)s:%(lineno)s %(funcName)s %(message)s"
handler = logging.FileHandler(cfg['LOG_FILE'])
handler.setFormatter(logging.Formatter(format_string))
app.logger.setLevel(cfg['LOG_LEVEL'].upper())
app.logger.addHandler(handler)


def clean_logs():
    current_date = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    app_log = cfg['LOG_FILE']
    app_log_size = os.path.getsize(app_log)
    app_gz_log = cfg['LOG_FILE'] + '.%s.gz' % (current_date)
    if os.path.getsize(app_log) >= cfg['LOG_SIZE']:
        file_in = open(app_log, 'rb')
        file_out = gzip.open(app_gz_log, 'wb')
        file_out.writelines(file_in)
        file_out.close()
        file_in.close()
        open(app_log, 'w').close()


Triangle(app)
from app import views
