from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField
from wtforms import validators, StringField, SubmitField
import json
import pyodbc
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
                    parsed_uri = urlparse(uiobj["burl"])
                    bdomain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                    id.flowStart(uiobj["bname"], uiobj["burl"], uiobj["btitle"], bdomain)
                    conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-1P8QTPD;''Database=CRFTest;''UID=Sanchit12;''PWD=GSWarrior02;''Trusted_Connection=yes;')
                    cur = conn.cursor()
                    postgres_insert_query = """SET ANSI_WARNINGS OFF; INSERT INTO BUSINESSES (business_name, business_url) \
                    VALUES (?, ?); SET ANSI_WARNINGS ON; """
                    record_to_insert = (uiobj["bname"], uiobj["burl"])
                    cur.execute(postgres_insert_query, record_to_insert)
                    conn.commit()
                    conn.close()
                    render_template('index.html', notify="success")
                else:
                    render_template('index.html', notify="error")
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
