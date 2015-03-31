# -*- coding: utf-8 -*-
from app import app, cfg, clean_logs
from flask import Flask, abort, jsonify, g, redirect, render_template, request, send_from_directory, session, url_for, \
    make_response
import ast, json, pickle, re, string, datetime
import controls
import os


@app.errorhandler(400)
def page_not_found(e):
    clean_logs()
    return render_template('400.html', language='en'), 400


@app.errorhandler(403)
def page_not_found(e):
    clean_logs()
    return render_template('403.html', language='en'), 403


@app.errorhandler(404)
def page_not_found(e):
    clean_logs()
    return render_template('404.html', language='en'), 404


@app.errorhandler(500)
def page_not_found(e):
    clean_logs()
    return render_template('500.html', language='en'), 500


@app.route('/generate', methods=['GET'])
def generator():
    clean_logs()
    return render_template('generate.html', language='en')


@app.route('/generate/insert', methods=['POST'])
def insert_docs():
    clean_logs()
    contents = request.get_json()['contents']
    _datetime = datetime.datetime.now().strftime('%S')
    filename = os.path.join(app.root_path, 'static\\files/') + _datetime + cfg[
        'EXTENSION']  # cfg['REPOSITORY'] + _datetime + cfg['EXTENSION']
    result = controls.files.generate_files(contents, filename)
    app.logger.debug(result)
    return make_response(result, 200)


@app.route('/generate/download/<path:filename>')
def download_file(filename):
    app.logger.debug(filename)
    return send_from_directory(os.path.join(app.root_path, 'static\\files/'), filename)  # cfg['REPOSITORY']


@app.route('/', methods=['GET'])
def index():
    clean_logs()
    return render_template('index.html', language='en')
