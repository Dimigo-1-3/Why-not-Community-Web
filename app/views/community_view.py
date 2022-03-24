from os import POSIX_FADV_SEQUENTIAL
from flask import render_template ,redirect, Blueprint, request, session
from app.mod import json_loader,form_checker
from app import db, models

bp = Blueprint('community', __name__, url_prefix='/community')

@bp.route("/question_view/<question_id>", methods=["GET"])
def question_view(question_id):
    if session.get("id",None) != None:
        Question_object = models.Question.query.filter_by(id=question_id).first()
        if Question_object:
            if Question_object.anonymous:
                username = "익명유저"
            else:
                username = models.User.query.filter_by(id = Question_object.owner_id).first().username
            answer_list = Question_object.list_answer()
            return render_template("question_view.html",
                                    username=username, 
                                    question_object=Question_object,
                                    answer_list=answer_list
                                )
        else:
            return render_template("error/404.html"), 404
@bp.route("/post_view/<post_id>", methods=["GET"])
def post_view(post_id):
    if session.get("id",None) != None:
        Post_object = models.Post.query.filter_by(id=post_id).first()
        if Post_object:
            if Post_object.anonymous:
                username = "익명유저"
            else:
                username = models.User.query.filter_by(id = Post_object.owner_id).first().username
            reply_list = Post_object.list_reply()
            return render_template("post_view.html",
                                    username=username, 
                                    post_object=Post_object,
                                    reply_list=reply_list
                                )
        else:
            return render_template("error/404.html"), 404
        