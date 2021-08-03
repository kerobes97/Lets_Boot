from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.survey_db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   

db = SQLAlchemy(app)

class Respondents(db.Model):
    __tablename__ = 'respondents'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable = False)
    age = db.Column(db.Integer())
    sex = db.Column(db.Integer()) #1 남자 2 여자

    plans = db.relationship('Plan', backref = 'plan')

    def __repr__(self):
        return f"ID:{self.id}, 이름:{self.name}, 나이:{self.age}, 성별:{self.sex}"


class Plan(db.Model):
    __tablename__ = 'plan'

    id = db.Column(db.Integer(), db.ForeignKey('respondents.id'), primary_key = True)
    s_month = db.Column(db.Integer())
    days = db.Column(db.Integer())
    T_Cost = db.Column(db.Integer())
    O_Cost = db.Column(db.Integer())
    T_Num = db.Column(db.Integer())
    spot = db.Column(db.Integer())
        #11 서울인천 / 21 울산부산 / 31 경기 / 32 강원 / 33 충북 / 34 대전충남 / 37 대구경북 / 38 경남 / 35 전북 / 36 전남광주 / 39 제주
    trans = db.Column(db.Integer())
        # 1 자가용 2 철도 3 항공선박 4 대중교통 5 차량렌트

    users = db.Column(db.Integer(), db.ForeignKey('users.id'))


    def __repr__(self):
        return f"ID: {self.id}, 여행일수: {self.days}, 수량: {self.type}, 교통수단: {self.trans}, 예산: {self.budget}, 동행 수: {self.partner_num}, 여행지: {self.city}"

db.create_all()