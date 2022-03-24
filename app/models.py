from re import T
from app import db
# from sqlalchemy import DateTime, ARRAY
import pytz, datetime
from werkzeug.security import generate_password_hash, check_password_hash
KST = pytz.timezone('Asia/Seoul')
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    def __init__(self,id,pw,username):
        self.id = id
        self.password = generate_password_hash(pw)
        self.username = username
    def change_pw(self, old_pw, new_pw):
        if check_password_hash(self.password, old_pw):
            self.password = generate_password_hash(new_pw)
            return True
        return False
    def check_pw(self,pw):
        return check_password_hash(self.password,pw)
class Question(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    owner_id = db.Column(db.Integer(), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(20), nullable=False)
    anonymous = db.Column(db.Boolean(), nullable=False)
    text = db.Column(db.String(5000), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    answer_id = db.Column(db.String(500), nullable=False)
    def __init__(self,owner_id,title,language,anonymous,text):
        self.owner_id = owner_id
        self.title = title
        self.language = language
        self.anonymous = anonymous
        self.text = text
        self.created_date = datetime.datetime.now(tz=KST)
        self.answer_id = ""
    def add_answer(self,new_answer_id):
        if len(self.answer_id) != 0:
            self.answer_id += ","
        self.answer_id += new_answer_id
    def list_answer(self):
        answer_id_list = self.answer_id.split(",")
        answer_list = []
        for i in range(0,len(answer_id_list)):
            answer_list.append(Answer.query.filter_by(id=int(answer_id_list[i])).first())
        return answer_list
class Answer(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    owner_id = db.Column(db.Integer(), nullable=False)
    text = db.Column(db.String(5000), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    question_id = db.Column(db.Integer(), nullable=False)
    approved = db.Column(db.Boolean, nullable=False)
    def __init__(self,owner_id,text,question_id):
        self.owner_id = owner_id
        self.text = text
        self.created_date = datetime.datetime.now(tz=KST)
        self.question_id = question_id
        self.approved = False
class Reply(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    owner_id = db.Column(db.Integer(), nullable=False)
    text = db.Column(db.String(300), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    post_id = db.Column(db.Integer(), nullable=False)
    def __init__(self,owner_id,text,question_id):
        self.owner_id = owner_id
        self.text = text
        self.created_date = datetime.datetime.now(tz=KST)
        self.post_id = question_id
class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    owner_id = db.Column(db.Integer(), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    anonymous = db.Column(db.Boolean(), nullable=False)
    text = db.Column(db.String(5000), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    reply_id = db.Column(db.String(500), nullable=False)
    def __init__(self,owner_id,title,anonymous,text):
        self.owner_id = owner_id
        self.title = title
        self.anonymous = anonymous
        self.text = text
        self.created_date = datetime.datetime.now(tz=KST)
        self.reply_id = ""