from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'letsAgreeToDisagree'


@app.route("/", methods=['GET', 'POST'])
def hello():

    # print(form.errors)
    if request.method == 'POST':
        render_template('index.html')
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
