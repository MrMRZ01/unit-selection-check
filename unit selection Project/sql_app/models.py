from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from database import Base

student_course = Table(
    'students_courses',
    Base.metadata,
    Column('student_id', String, ForeignKey('students.Sid')),
    Column('course_id', String, ForeignKey('courses.cid'))
)

course_teacher = Table(
    'courses_teachers',
    Base.metadata,
    Column('course_id', String, ForeignKey('courses.cid')),
    Column('teacher_id', String, ForeignKey('teachers.Tid'))
)

student_teacher = Table(
    'student_teacher',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.Sid')),
    Column('teacher_id', Integer, ForeignKey('teachers.Tid'))
)

class Course(Base):

    __tablename__ = "courses"

    cid = Column(Integer, primary_key=True)
    cname = Column(String)
    department = Column(String)
    credit = Column(Integer)
    students = relationship("Student", secondary=student_course, back_populates="courses")
    teachers = relationship("Teacher", secondary=course_teacher, back_populates="courses")

class Teacher(Base):

    __tablename__ = "teachers"

    Tid = Column(String, primary_key=True)
    Tname = Column(String)
    TLname = Column(String)
    Tmajor = Column(String)
    Tbirth = Column(String)
    Tborn = Column(String)
    Taddress = Column(String)
    Tpostal = Column(String)
    Tphone = Column(String)
    THphone = Column(String)
    Tcourseids = relationship("Course", secondary=course_teacher, back_populates="teachers")
    TNid = Column(String)
    Tdepartment = Column(String)
    Tids = relationship("Teacher", secondary=student_teacher, back_populates="students")

class Student(Base):

    __tablename__ = "students"

    Sid = Column(String, primary_key=True)
    Sname = Column(String)
    SLname = Column(String)
    Sfather = Column(String)
    Sids = Column(String) #سریال شناسنامه
    Smajor = Column(String)
    Sbirth = Column(String)
    Sborn = Column(String)
    Saddress = Column(String)
    Spostal = Column(String)
    Sphone = Column(String)
    SHphone = Column(String)
    Courses_ids = Column(String)
    Teachers_ids = Column(String)
    Scourseids = relationship("Course", secondary=student_course, back_populates="students")
    SNid = Column(String)
    Smarried = Column(String)
    Sdepartment = Column(String)
    course_numbers = Column(String)
    Tids = relationship("Teacher", secondary=student_teacher, back_populates="students")