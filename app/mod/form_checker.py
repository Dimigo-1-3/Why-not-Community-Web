import re
from app.mod import json_loader
def regex_checker(text, regex):
    p = re.compile(regex)
    return p.match(text)
def pw_checker(pw):
    regex ='''^(?=.*[a-z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15}''' #영어,숫자,특수 포함 8에서 15자
    return regex_checker(pw, regex)
def id_checker(id):
    regex = '''13([0-3])([0-9])'''
    return regex_checker(id, regex) and int(id) <= 1332
def validation1_checker(val):
    return val == "웹펭"
def validation2_checker(val):
    return val == "박세환"

def signup_checker(id,pw,username,val1,val2):
    if not id_checker(id):
        return "올바르지 않은 학번 형식 입니다"
    if not pw_checker(pw):
        return "올바르지 않은 비밀번호 형식 입니다"
    if len(username) > 3 or len(username) < 2:
        return "올바르지 않은 이름 입니다"
    if val1 !="웹펭" or val2 != "박세환":
        return "올바르지 않은 인증질문 답입니다"
    return True