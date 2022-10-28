from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,Date # ประเภทของ columns มีอะไรบ้าง
from flask_login import UserMixin
# from flask_wtf import wtforms # pip install Flask-WTF
# from wtforms import StringField , PasswordField , SubmitField
# from wtforms.validators import InputRequired ,Length ,ValidationError

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:RTTooa27373@node37431-project.proen.app.ruk-com.cloud:5432/login' # define ของ databaseSQL ดึง database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # ปิดข้อความโชว์ ถ้าจะเปิดให้เป็น True
app.config['SQLALCHEMY_KEY'] = 'secretkey' 

class User(db.Model,UserMixin):
    __tablename__ = 'comments' # เรียกใช้ table ที่ชื่อว่า comments
    id = Column(Integer,primary_key=True) # primary_key คือซ้ำไม่ได้
    Username = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
# class RegisterForm(FlaskFrom):
#     username = StringField(validators=[InputRequired() , Length(
#         min=4 , max=20)], render_kw={"placeholder":"Username"})

#     password = StringField(validators=[InputRequired() , Length(
#         min=4 , max=20)], render_kw={"placeholder":"Password"})
    
    # submit = SubmitField("Register")
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/main/login')
def login():

    return render_template('login.html')

@app.route('/main/register')
def register():

    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
