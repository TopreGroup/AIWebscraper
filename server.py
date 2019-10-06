#!/usr/bin/env python3

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField
from wtforms import validators, StringField, SubmitField
import json
import pytds
from urllib.parse import urlparse
import id

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'letsAgreeToDisagree'


@app.route("/", methods=['GET', 'POST'])
def trance():

    if request.method == 'POST':
        if request.data:
            uiobjs = (json.loads(request.data.decode("utf-8")))
            print(uiobjs)
            for uiobj in uiobjs:
                if(uiobj["bname"] and uiobj["burl"] and uiobj["btitle"]):
                    conn = pytds.connect('devdb.trunked.com.au', 'trunkedproject', 'trunkedproject', 'rmitProject@trunked')
                    cur = conn.cursor()
                    postgres_insert_query = """SET ANSI_WARNINGS OFF; INSERT INTO BUSINESSES (business_name, business_url) \
                    VALUES (%s, %s); SET ANSI_WARNINGS ON; """
                    parsed_uri = urlparse(uiobj["burl"])
                    bdomain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                    record_to_insert = (uiobj["bname"], bdomain)
                    cur.execute(postgres_insert_query, record_to_insert)
                    conn.commit()
                    conn.close()
                    id.flowStart(uiobj["bname"], uiobj["burl"], uiobj["btitle"], bdomain)
                    render_template('index.html', notify="success")
                else:
                    render_template('index.html', notify="error")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
