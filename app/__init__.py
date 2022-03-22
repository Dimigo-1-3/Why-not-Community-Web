
from flask import Flask, render_template, request, session, redirect, url_for, flash, g
from flask_sqlalchemy import SQLAlchemy
import secrets,os

base_dir = os.path.abspath(os.path.dirname(__file__))

db_file = os.path.join(base_dir, "db.sqlite")

app = Flask(__name__)
app.secret_key = secrets.token_bytes(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file
db = SQLAlchemy(app)

from app.views import main_view, auth_view
from app import models
@app.before_request
def add_global():
    id = session.get("id")
    if id != None:
        User_object = models.User.query.filter_by(id=id).first()
        g.user = (id,User_object.username)

app.register_blueprint(main_view.bp)
app.register_blueprint(auth_view.bp)
db.init_app(app)
db.app = app
db.create_all()
