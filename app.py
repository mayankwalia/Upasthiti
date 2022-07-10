from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'


db=SQLAlchemy(app)

class Member():
    memberId = db.Column(db.Integer, primary_key =True,autoincrement=True)
    firstName = db.Column(db.String(100), nullable = False)
    lastName = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(150), nullable = False)
    memberType= db.Column(db.String(3),nullable=False)
    sapId=db.Column(db.Integer,primary_key=True)
    mobileNo=db.Column(db.String(10))



class Programs(db.Model):
    programId=db.Column(db.Integer,autoincrement=True,primary_key=True)
    programCode=db.Column(db.String,unique=True,nullable=False)
    programName=db.Column(db.String,unique=True,nullable=False)
    duration=db.Column(db.Integer,nullable=False)
    departmentId=db.Column(db.Integer,db.ForeignKey('department.departmentId'),nullable=False)


class Student(db.Model):
    memberId = db.Column(db.Integer, db.ForeignKey('member.memberId'),nullable=False)
    rollNumber=db.Column(db.Integer,nullable=False)
    sapId=db.Column(db.Integer,primary_key=True)
    programId=db.Column(db.Integer, db.ForeignKey('programs.programId'),nullable=False)

class Faculty(db.Model):
    memberId = db.Column(db.Integer, db.ForeignKey('member.memberId'),nullable=False)
    facultyId=db.Column(db.Integer,nullable=False)
    sapId=db.Column(db.Integer,primary_key=True)
    departmentId=db.Column(db.Integer, db.ForeignKey('department.departmentId'),nullable=False)

class Staff(db.Model):
    memberId = db.Column(db.Integer, db.ForeignKey('member.memberId'),nullable=False)
    staffId=db.Column(db.Integer,nullable=False,primary_key=True)
    # sapId=db.Column(db.Integer,primaryKey=True)

class Admin(db.Model):
    memberId = db.Column(db.Integer, db.ForeignKey('member.memberId'),nullable=False)
    sapId=db.Column(db.Integer,primary_key=True)
    viewLevel=db.Column(db.Integer,nullable=False)


class Course(db.Model):
    courseId=db.Column(db.Integer,autoincrement=True,primary_key=True)
    code=db.Column(db.String,unique=True,nullable=False)
    name=db.Column(db.String,nullable=False)
    description=db.Column(db.String)
    facultyId=db.Column(db.Integer, db.ForeignKey('faculty.facultyId'))

class Enrollments(db.Model):
    enrollmentId=db.Column(db.Integer,autoincrement=True,primary_key=True)
    studentId=db.Column(db.Integer,db.ForeignKey('student.studentId'),nullable=False)
    courseId=db.Column(db.Integer,db.ForeignKey('course.courseId'),nullable=False)

class Department(db.Model):
    departmentId=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String,unique=True,nullable=False)
    hodId=db.Column(db.Integer,db.ForeignKey('faculty.facultyId'))
    buildingId=db.Column(db.Integer,db.ForeignKey('building.buildingId'))

class Building(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String,unique=True,nullable=False)
    location=db.Column(db.String)


class Attendance(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    time=db.Column(db.Time,default=datetime.datetime.now())
    memberId=db.Column(db.Integer,db.ForeignKey('member.memberId'),nullable=False)
    buildingId=db.Column(db.Integer,db.ForeignKey('building.buildingId'),nullable=False)
    flag=db.Column(db.String,nullable=False)






@app.route('/')
def home():
    return render_template('addMember.html')

if __name__=="__main__":
    app.run(debug=True)