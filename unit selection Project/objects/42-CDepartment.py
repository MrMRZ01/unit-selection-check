from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/home/{CDepartment}")
def CD(CDepartment: str):
    allDepartment1 = ["فنی و مهندسی","علوم پایه",
                  "شیمی","اقتصاد",'ادبیات', "دامپزشکی"]


    if CDepartment not in allDepartment1:
        raise HTTPException(detail="دانشکده وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return "دانشکده وارد شده ثبت شد."


