from flask import render_template ,redirect, Blueprint, request, session
from app.mod import json_loader,form_checker
from app import db, models

bp = Blueprint('community', __name__, url_prefix='/community')

@bp.route("/view", methods=["GET", "POST"])
def view():
    if session.get("id",None) != None:
        if request.method == "POST":
            raise NotImplementedError
        else:
            raise NotImplementedError
            return render_template("community_view.html")