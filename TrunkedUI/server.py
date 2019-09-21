from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField
from wtforms import validators, StringField, SubmitField
import json
import id

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'letsAgreeToDisagree'


@app.route("/", methods=['GET', 'POST'])
def trance():

    if request.method == 'POST':
        if request.data:
            uiobj = (json.loads(request.data.decode("utf-8")))[0]
            if(uiobj["bname"] and uiobj["burl"] and uiobj["btitle"]):
                render_template('index.html', notify="success")
            else:
                render_template('index.html', notify="error")
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
