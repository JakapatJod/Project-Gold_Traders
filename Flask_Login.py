from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
# from Flask_Login import UserMixin
# from flask_wtf import wtforms # pip install Flask-WTF
# from wtforms import StringField , PasswordField , SubmitField
# from wtforms.validators import InputRequired ,Length ,ValidationError

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:RTTooa27373@10.104.4.188:5432/login' # define ของ databaseSQL ดึง database
app.config['SQLALCHEMY_KEY'] = 'secretkey' 

# class User(db.Model,UserMixin):
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(20),nullable=False,unique=True)
#     password = db.Column(db.String(80), nullable=False)

# class RegisterForm(FlaskFrom):
#     username = StringField(validators=[InputRequired() , Length(
#         min=4 , max=20)], render_kw={"placeholder":"Username"})

#     password = StringField(validators=[InputRequired() , Length(
#         min=4 , max=20)], render_kw={"placeholder":"Password"})
    
#     submit = SubmitField("Register")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
