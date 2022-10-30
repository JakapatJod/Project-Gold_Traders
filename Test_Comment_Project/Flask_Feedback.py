from flask import Flask,render_template,request,redirect,url_for  # ตอนนี้ run เป็น Local เซิฟ
from flask_sqlalchemy import SQLAlchemy # มาทำเพื่อ DB model ใน columns
from sqlalchemy import Column,Integer,String,Date # ประเภทของ columns มีอะไรบ้าง
import psycopg2  
import psycopg2.extras

app =  Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:DMSgax19890@10.104.9.215:5432/feedbacks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # ปิดข้อความโชว์ ถ้าจะเปิดให้เป็น True

db = SQLAlchemy(app)


@app.route('/')
def index():
    connection = psycopg2.connect(user='webadmin',
                                    password='DMSgax19890',
                                    host='node38438-project.proen.app.ruk-com.cloud',
                                    port='11260',
                                    database='feedbacks')
    cursor = connection.cursor()
    postgresSQL_select_Query = "select * from feed where username = %s and comment = %s "
    cursor.execute(postgresSQL_select_Query)
    Data_all = cursor.fetchall()
    
    result = Data_all
    return render_template('index.html',result=result) # result คือ ข้อมูลที่ดึงออกมาทั้งหมด

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/process',methods=['POST'])
def process():
    if request.method=='POST':
        try:
  
            name = request.form['name']
            comment = request.form['comment']
            connection = psycopg2.connect(user='webadmin',
                                            password='DMSgax19890',
                                            host='node38438-project.proen.app.ruk-com.cloud',
                                            port='11260',
                                            database='login')
            cursor = connection.cursor()
            
            postgres_insert_query = """ INSERT INTO accounts (username, email , comment) VALUES (%s,%s,%s)"""
            record_to_insert = (name,comment)
            cursor.execute(postgres_insert_query,record_to_insert)
            connection.commit()

        finally:
            if connection:
                cursor.close()
                connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

