from flask import Flask,render_template,request,redirect,url_for  # ตอนนี้ run เป็น Local เซิฟ
from flask_sqlalchemy import SQLAlchemy # มาทำเพื่อ DB model ใน columns
from sqlalchemy import Column,Integer,String,Date # ประเภทของ columns มีอะไรบ้าง

app =  Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:DMSgax19890@10.104.9.215:5432/feedbacks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # ปิดข้อความโชว์ ถ้าจะเปิดให้เป็น True

db = SQLAlchemy(app)

class Feedback(db.Model): 
    __tablename__ = 'feedback' # เรียกใช้ table ที่ชื่อว่า comments
    id = Column(Integer,primary_key=True) # primary_key คือซ้ำไม่ได้
    name = Column(String,nullable=False)
    email = Column(String)
    comment = Column(String)

@app.route('/')
def index():
    result = Feedback.query.all()
    return render_template('index.html',result=result) # result คือ ข้อมูลที่ดึงออกมาทั้งหมด

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/process',methods=['POST'])
def process():  
    name = request.form['name']
    comment = request.form['comment']
    signature = Feedback(name=name,comment=comment)
    db.session.add(signature)   
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

