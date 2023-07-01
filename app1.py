from flask import Flask,render_template,request
import mysql.connector
user_dict={'admin':'1234','user':'5678'}
conn = mysql.connector.connect(host='leenpm.mysql.pythonanywhere-services.com',user='leenpm',password='naskas123',database='leenpm$default')
mycursor=conn.cursor()
#create a flask application
app = Flask(__name__)

#Define the route

@app.route('/')
def hello():
    return render_template('first.html')
@app.route('/employee')
def employee():
    return render_template('emp.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/department')
def department():
    return render_template('department.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/home',methods=['POST'])
def home():
    uname=request.form['username']
    pwd=request.form['password']

    if uname not in user_dict:
        return render_template('login.html',msg='Invalid User')
    elif user_dict[uname] != pwd:
        return render_template('login.html',msg='Invalid Password')
    else:
        return render_template('home.html')
@app.route('/view')
def view():
    query="SELECT * FROM employees"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/search')
def searchpage():
    return render_template('search.html')


@app.route('/searchresult',methods=['POST'])
def search():
    empid = request.form['emp_id']
    query="SELECT * FROM employees WHERE EMP_ID="+empid
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/add')
def add():
    return render_template('emp.html')

@app.route('/read',methods=['POST'])
def read():
    empid = request.form['empid']
    ename = request.form['empname']
    salary= request.form['salary']
    dept = request.form['dept']
    email = request.form['email']
    query = "INSERT INTO employees(EMP_ID,EMP_NAME,EMP_SALARY,EMP_DEPT,EMAIL_ID) VALUES (%s,%s,%s,%s,%s)"
    data = (empid,ename,salary,dept,email)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('emp.html',msgdata='Added Successfully')

