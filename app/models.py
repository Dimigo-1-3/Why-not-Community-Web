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
    text = db.Column(db.String(5000), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    answer_id = db.Column(db.String(500), nullable=False)
    def __init__(self,owner_id,title,language,text):
        self.owner_id = owner_id
        self.title = title
        self.language = language
        self.text = text
        self.created_date = datetime.datetime.now(tz=KST)
        self.answer_id = ""
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
        self.answer_id = question_id
        self.approved = False