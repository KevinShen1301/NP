import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
from flask_mail import Mail
from flask_mail import Message



app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] =  True
app.config['MAIL_USE_SSL']= False
app.config['MAIL_USERNAME']= 'nptest3697438@outlook.com'
app.config['MAIL_PASSWORD']= '12345Banana'
mail = Mail(app)

'''
conn = mysql.connect()
cursor = conn.cursor()
 

sql = "INSERT INTO ports(number) VALUES( %s)"   

for i in range(700,1001):


    data = (i,)
    cursor.execute(sql, data)
    conn.commit()

cursor.close()
conn.close()
'''
@app.route('/addports', methods=['POST'])
def add_user():
    try:
        _json = request.json
        _studentid = _json['studentid']
        

        if _studentid and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM ports")
            rows = cursor.fetchall()
            ports = []
            for row in rows:
                ports.append(row['number'])
                

            cursor.close()

            sql = "INSERT INTO student(studentid, port1, port2) VALUES( %s,%s, %s)"
            data = (_studentid, ports[0],ports[1],)
            
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()

            cursor = conn.cursor()
            sql = "DELETE FROM ports WHERE number = %s"
            data = {ports[0],}
            cursor.execute(sql, data)
        
           
            conn.commit()
            
            cursor.close()
            cursor = conn.cursor()
            sql = "DELETE FROM ports WHERE number = %s"
            data = {ports[1],}
            cursor.execute(sql, data)
            
           
            conn.commit()
            
            cursor.close()
            
            return {"port1":ports[0],"port2":ports[1]}
        else:
            return jsonify('Fail')
    except Exception as e:
        print(e)
    finally:
       
        conn.close()


@app.route('/mailservice',methods = ['POST'])
def sendmail():
    _json = request.json
    _port1 = _json['port1']
    _port2 = _json['port2']
    
    if _port1 and _port2 and request.method == 'POST':

        _message = 'port1:'+str(_port1)+'port2:'+str(_port2)
        print (_message)
        msg = Message('Your ports number',sender=('nptest3697438@outlook.com'),recipients = ['kevinshen1301@hotmail.com'])
        msg.body = _message
        mail.send(msg)
        return 'Message sent'
    else:
        return 'Fail'
if __name__ == "__main__":
    app.run()
