from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/home/{StudentDepartment}")
def StudentDepartment(StudentDepartment: str):
    allDepartment = ["فنی و مهندسی","علوم پایه",
                  "شیمی","اقتصاد",'ادبیات', "دامپزشکی"]


    if StudentDepartment not in allDepartment:
        raise HTTPException(detail="دانشکده وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return "دانشکده وارد شده، ثبت شد."


