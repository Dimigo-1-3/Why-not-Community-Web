
from flask import render_template, request, session, redirect, url_for,Blueprint, flash, g 
from app.mod import json_loader,form_checker
from app import db, models

message = json_loader.load_message().Auth #Load Message Object

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/signin", methods=["GET","POST"])
def signin():
    if session.get("id", None) == None:
        if request.method == "POST":
            id = request.form["id"]
            pw = request.form["pw"]
            User_object = models.User.query.filter_by(id=id).first()
            if User_object:
                if User_object.check_pw(pw):
                    session['id']=id
                    session['username'] = User_object.username
                    return redirect(url_for("main.index"))
            flash(message.wrong_id_or_pw)
            return render_template("signin.html")
        return render_template("signin.html")
    else:
        return redirect(url_for("main.index"))
@bp.route("/signup",methods=["GET","POST"])
def signup():
    if session.get("id", None) == None:
        if request.method == "POST":
            id = request.form["id"]
            pw = request.form["pw"]
            username = request.form["username"]
            val1 = request.form["val"]
            val2 = request.form["valtwo"]
            regex_result = form_checker.signup_checker(id,pw,username,val1,val2)
            if type(regex_result) == str:
                flash(regex_result)
                return render_template("signup.html")
            User_object = models.User.query.filter_by(id=id).first()
            if User_object:
                flash("이미 가입된 ID입니다. 만약, 자신이 가입하지 않았다면 관리자에게 문의하세요")
                print(User_object.id)
                return render_template("signup.html")
            user = models.User(id,pw,username)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("main.index"))
        else:
            return render_template("signup.html")
@bp.route("/logout", methods=["GET"])
def logout():
    if session.get("id", None) != None:
        session.clear()
    return redirect(url_for("main.index"))
