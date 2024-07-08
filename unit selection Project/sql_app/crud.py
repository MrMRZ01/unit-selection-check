from sqlalchemy.orm import Session
from . import models, schemas


def set_course(db, table, courses):
    for course in courses:
        course = get_Course(db, int(course))
        table.SCourseIDs.append(course)

def set_teacher(db, table, teachers):
    for teacher in teachers:
        teacher = get_Teacher(db, int(teacher))
        table.LIDs.append(teacher)

def set_teacher_course(db, table, courses):
    for course in courses:
        course = get_Course(db, int(course))
        table.LCourseIDs.append(course)




def get_Course(db: Session, cid: int):
    return db.query(models.Course).filter(models.Course.cid == cid).first()

# def get_lesson(db: Session, id: int):
#     return db.query(models.Lesson).filter(models.Lesson.CID == id).first()



def create_Course(db: Session, course: schemas.Course):
    db_course = models.Course(cid=course.cid,
                              cname=course.cname,
                              department=course.department,
                              credit=course.credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return "درس با موفقیت ساخته شد."

def delete_Course(db: Session):
    db.query(models.Course).filter(models.Course)
    db.delete(db.query(models.Course).filter(models.Course))
    return "با موفقیت حذف شد."

def patch_Course(db: Session, course: schemas.Course):
    db_course = models.Course(cid=course.cid, cname=course.cname, department=course.department, credit=course.credit)
    db.query(models.Course).filter(models)
    db.delete(db.query(models.Course).filter(models))
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return "درس با موفقیت آپدیت شد."

# -------------------------------------------------------------------------------------------------------------------

# استاد:

def get_Teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.Tid == teacher_id).first()



def create_Teacher(db: Session, Teacher: schemas.Teacher):
    db_teacher = models.Teacher(
        Tid=Teacher.Tid, #کداستادی
        Tname=Teacher.Tname,
        TLname=Teacher.TLname, #فامیلی
        Tmajor=Teacher.Tmajor, #رشته تحصیلی
        Tbirth=Teacher.Tbirth, #تاریخ تولد
        Tborn=Teacher.Tborn, #محل تولد
        Taddress=Teacher.Taddress,
        Tpostal=Teacher.Tpostal, #کدپستی
        Tphone=Teacher.Tphone,
        THphone=Teacher.THphone, #تلفن ثابت
        Tcuorseid=Teacher.Tcuorseid, #کد دروس ارایه شده
        TNid=Teacher.TNid, #کدملی استاد
        Tdepartment=Teacher.Tdepartment #دانشکده
    )
    set_teacher_course(db, db_teacher, Teacher.LCourseIDs.split(","))
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return "با موفقیت ساخته شد."

def delete_Teacher(db: Session):
    db.query(models.Teacher).filter(models.Teacher)
    db.delete(db.query(models.Teacher).filter(models.Teacher))
    return "با موفقیت حذف شد."

def patch_Teacher(db: Session, Teacher: schemas.Teacher):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.Tid == Teacher.Tid).first()
    db_teacher.Tname=Teacher.Tname
    db_teacher.TLname=Teacher.TLname
    db_teacher.Tmajor=Teacher.Tmajor
    db_teacher.Tbirth=Teacher.Tbirth
    db_teacher.Tborn=Teacher.Tborn
    db_teacher.Taddress = Teacher.Taddress
    db_teacher.Tpostal = Teacher.Tpostal
    db_teacher.Tphone = Teacher.Tphone
    db_teacher.THphone = Teacher.THphone
    db_teacher.Tcuorseid = Teacher.Tcuorseid
    db_teacher.TNid = Teacher.TNid
    db_teacher.Tdepartment = Teacher.Tdepartment

    db_teacher.LCourseIDs = []
    set_teacher_course(db, db_teacher, Teacher.LCourseIDs.split(","))
    db.commit()
    return "با موفقیت آپدیت شد"
# -----------------------------------------------------------------------------------------------
# دانشجو:

def get_Student(db: Session, Student_Sid: int):
    return db.query(models.Student).filter(models.Student.id == Student_Sid).first()



def create_Student(db: Session, Student: schemas.Student):
    db_Student = models.Student(
        Sid=Student.Sid, #کداستادی
        Sname=Student.Sname,
        SLname=Student.SLname, #فامیلی
        Smajor=Student.Smajor, #رشته تحصیلی
        Sbirth=Student.Sbirth, #تاریخ تولد
        Sborn=Student.Sborn, #محل تولد
        Saddress=Student.Saddress,
        Spostal=Student.Spostal, #کدپستی
        Sphone=Student.Sphone,
        SHphone=Student.SHphone, #تلفن ثابت
        Scuorseid=Student.Scuorseid, #کد دروس ارایه شده
        SNid=Student.SNid, #کدملی استاد
        Sdepartment=Student.Sdepartment, #دانشکده,
        course_numbers=Student.course_numbers
    )


    for course in Student.course_numbers.split(","):
        course = get_Course(db, int(course))
        db_Student.Scuorseid.append(course)


    db.add(db_Student)
    db.commit()
    db.refresh(db_Student)
    return db_Student

def delete_Student(db: Session):
    db.query(models.Student).filter(models.Student)
    db.delete(db.query(models.Student).filter(models.Student))
    return "با موفقیت حذف شد."

def patch_Student(db: Session, Student: schemas.Student):

    db_student = db.query(models.Student).filter(models.Student.Sid == Student.Sid).first()
    db_student.Sname=Student.Sname
    db_student.SLname=Student.SLname
    db_student.Smajor=Student.Smajor
    db_student.Sbirth=Student.Sbirth
    db_student.Sborn=Student.Sborn
    db_student.Saddress = Student.Saddress
    db_student.Spostal = Student.Spostal
    db_student.Sphone = Student.Sphone
    db_student.SHphone = Student.SHphone
    db_student.Scuorseid = Student.Scuorseid
    db_student.SNid = Student.SNid
    db_student.Sdepartment = Student.Sdepartment
    db_student.course_numbers = Student.course_numbers
    db_student.SLid = Student.SLid

    db.query(models.Student).filter(models)
    db.delete(db.query(models.Student).filter(models))
    db.add(db_student)

    db_student.SCourseIDs = []
    db_student.LIDs = []
    set_course(db, db_student, Student.Scuorseid.split(","))
    set_teacher(db, db_student, Student.SLid.split(","))


    db.commit()
    db.refresh(db_student)
    return "با موفقیت آپدیت شد."