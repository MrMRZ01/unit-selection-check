from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/CreateCou/", response_model=schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_Course(db=db, course=course)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return crud.create_Course(db=db, course=course)

@app.get("/GetCou/{course_id}", response_model=schemas.Course)
def read_Course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_Course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course
@app.delete("/DeleteCou/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_Course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    crud.delete_Course(db, course_id=course_id)
    return {"message": "Course deleted successfully"}

@app.patch("/UpdateCou/{course_id}", response_model=schemas.Course)
def update_course(course_id: int, course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_Course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return crud.patch_Course(db, course_id=course_id, course=course)
# -----------------------------------------------------------------------------------
#استاد

@app.post("/CreateTeacher/", response_model=schemas.Teacher)
def create_Teacher(Teacher: schemas.Teacher, db: Session = Depends(get_db)):
    db_Teacher = crud.get_Teacher(db, Teacher_id=Teacher.Tid)
    if db_Teacher:
        raise HTTPException(status_code=400, detail="Teacher already exists")
    return crud.create_Teacher(db=db, Teacher=Teacher)

@app.get("/GetTeacher/{Teacher_id}", response_model=schemas.Teacher)
def read_Teacher(Teacher_id: int, db: Session = Depends(get_db)):
    db_Teacher = crud.get_Teacher(db, Teacher_id=Teacher_id)
    if db_Teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_Teacher

@app.delete("/DeleteTeacher/{Teacher_id}")
def delete_Teacher(Teacher_id: int, db: Session = Depends(get_db)):
    db_Teacher = crud.get_Teacher(db, Teacher_id=Teacher_id)
    if db_Teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    crud.delete_Teacher(db, Teacher_id=Teacher_id)
    return {"message": "Teacher deleted successfully"}

@app.patch("/UpdateTeacher/{Teacher_id}", response_model=schemas.Teacher)
def update_Teacher(Teacher_id: int, Teacher: schemas.Teacher, db: Session = Depends(get_db)):
    db_Teacher = crud.get_Teacher(db, Teacher_id=Teacher_id)
    if db_Teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return crud.patch_Teacher(db, Teacher_id=Teacher_id, Teacher=Teacher)
# --------------------------------------------------------------------------------------
# دانشجو:

@app.post("/CreateStudent/", response_model=schemas.Student)
def create_Student(Student: schemas.Student, db: Session = Depends(get_db)):
    db_Student = crud.get_Student(db, Student_id=Student.Sid)
    if db_Student:
        raise HTTPException(status_code=400, detail="Student already exists")
    return crud.create_Student(db=db, Student=Student)

@app.get("/GetStudent/{Student_id}", response_model=schemas.Student)
def read_Student(Student_id: int, db: Session = Depends(get_db)):
    db_Student = crud.get_Student(db, Student_id=Student_id)
    if db_Student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_Student

@app.delete("/DeleteStudent/{Student_id}")
def delete_Student(Student_id: int, db: Session = Depends(get_db)):
    db_Student = crud.get_Student(db, Student_id=Student_id)
    if db_Student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    crud.delete_Student(db, Student_id=Student_id)
    return {"message": "Student deleted successfully"}

@app.patch("/UpdateStudent/{Student_id}", response_model=schemas.Student)
def update_Student(Student_id: int, Student: schemas.Student, db: Session = Depends(get_db)):
    db_Student = crud.get_Student(db, Student_id=Student_id)
    if db_Student is None:
        raise HTTPException(status_code=404, detail="Studente not found")
    return crud.patch_Student(db, Student_id=Student_id, Student=Student)

# -----------------------------------------------------------------------------------------
# اصلاح کد:

# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session
#
# from . import crud, models, schemas
# from .database import SessionLocal, engine
#
# models.Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
#
# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# @app.post("/create_course/", response_model=schemas.Course)
# def create_course(course: schemas.Course, db: Session = Depends(get_db)):
#     try:
#         db_course = crud.get_course(db, course_id=course.cid)
#         if db_course:
#             raise HTTPException(status_code=400, detail="Course already exists")
#         return crud.create_course(db=db, course=course)
#     except Exception as e:
#         # مدیریت خطا
#         print(f"خطا در ایجاد دوره: {e}")
#
# @app.get("/get_course/{course_id}", response_model=schemas.Course)
# def read_course(course_id: int, db: Session = Depends(get_db)):
#     db_course = crud.get_course(db, course_id=course_id)
#     if db_course is None:
#         raise HTTPException(status_code=404, detail="Course not found")
#     return db_course
#
# # -----------------------------------------------------------------------------------
# # Teacher
#
# @app.post("/create_teacher/", response_model=schemas.Teacher)
# def create_teacher(teacher: schemas.Teacher, db: Session = Depends(get_db)):
#     try:
#         db_teacher = crud.get_teacher(db, teacher_id=teacher.tid)
#         if db_teacher:
#             raise HTTPException(status_code=400, detail="Teacher already exists")
#         return crud.create_teacher(db=db, teacher=teacher)
#     except Exception as e:
#         # مدیریت خطا
#         print(f"خطا در ایجاد استاد: {e}")
#
# @app.get("/get_teacher/{teacher_id}", response_model=schemas.Teacher)
# def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
#     db_teacher = crud.get_teacher(db, teacher_id=teacher_id)
#     if db_teacher is None:
#         raise HTTPException(status_code=404, detail="Teacher not found")
#     return db_teacher
#
# # --------------------------------------------------------------------------------------
# # Student
#
# @app.post("/create_student/", response_model=schemas.Student)
# def create_student(student: schemas.Student, db: Session = Depends(get_db)):
#     try:
#         db_student = crud.get_student(db, student_id=student.sid)
#         if db_student:
#             raise HTTPException(status_code=400, detail="Student already exists")
#         return crud.create_student(db=db, student=student)
#     except Exception as e:
#         # مدیریت خطا
#         print(f"خطا در ایجاد دانشجو: {e}")
#
# @app.get("/get_student/{student_id}", response_model=schemas.Student)
# def read_student(student_id: int, db: Session = Depends(get_db)):
#     db_student = crud.get_student(db, student_id=student_id)
#     if db_student is None:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return db_student