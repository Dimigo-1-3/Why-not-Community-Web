from flask import render_template, request, session, redirect, url_for,Blueprint
from app import models
from app.mod import json_loader

message = json_loader.load_message() #Load Message Object

bp = Blueprint('main', __name__, url_prefix='')

@bp.route("/")
def index():
    return render_template("index.html")