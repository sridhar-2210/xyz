from flask import Flask,render_template,request,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__,instance_relative_config=True)
app.secret_key='nuero'
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///../dbms/instance/test.db'
db=SQLAlchemy(app)
class user(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  firstname=db.Column(db.String(200),nullable=False)
  lastname=db.Column(db.String(200),nullable=False)
  address=db.Column(db.String(1000),nullable=False)
  password=db.Column(db.String(20),nullable=False)
  dateofbirth=db.Column(db.Date,nullable=False)
  username=db.Column(db.String(200),nullable=False)
  mob_num=db.Column(db.String(15),nullable=False)
  mail=db.Column(db.String(200),nullable=False)
  def __repr__(self):
    return "<user %r>" % self.id
@app.route('/profile')
def profile():
    userid = session.get("user_id")
    if userid is None:
        # Handle case where user_id is not found in session
        return redirect(url_for('home'))
    tasks = user.query.get(userid)
    if tasks is None:
        # Handle case where user_id doesn't exist in the database
        return redirect(url_for('home'))
    return render_template("profile.html", user=tasks)
@app.route('/login',methods=["POST","GET"])
def login():
  if request.method=="POST":
    username=request.form["username"]
    password=request.form["password"]
    try:
      tasks=user.query.filter_by(username=username,password=password).first()
      session['user_id']=tasks.id
    except Exception as e:
      return str(e)
    return render_template("home.html",user=tasks)
  else:
    return render_template("login.html")
@app.route('/home')
def home():
  return render_template('home.html')
@app.route('/signup',methods=["POST","GET"])
def signup():   
  if request.method=="POST":
    new_task=user()
    new_task.firstname=request.form["firstname"]  
    new_task.lastname=request.form["lastname"]
    new_task.address=request.form["address"]
    new_task.password=request.form["password"]
    new_task.username=request.form["username"]
    new_task.mob_num=request.form["mob_num"]
    new_task.mail=request.form["mail"]
    try:
      dob = datetime.strptime(request.form["dateofbirth"], '%Y-%m-%d').date()  # Convert to a date object
      new_task.dateofbirth=dob
    except ValueError:
      return "Invalid date format. Please use YYYY-MM-DD."
    try:
      db.session.add(new_task)
      db.session.commit()
      return redirect('/')
    except Exception as e:
      return "There is an issue"+str(e)
  else:
    return render_template("signup.html")
@app.route('/cart1')
def cart1():
  return render_template("cart1.html")
@app.route('/')
def index():
  return render_template("index.html")
if __name__== "__main__":
  app.run(debug=True)