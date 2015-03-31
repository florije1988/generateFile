# -*- coding: utf-8 -*-
from app import app, cfg, abort
import datetime, pickle, re, docx


def generate_files(content, filename):
    try:
        document = docx.Document()
        document.add_heading(' Test document', 0)
        p = document.add_paragraph(content)
        document.save(filename)
        return filename.split('/')[-1].split('.')[0]
    except Exception, e:
        app.logger.error(e)
        abort(500)
