from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/home/{StudentMajor}")
def StudentMajor(StudentMajor: str):
    allmajor = ["برق","کامپیوتر",
                  "عمران","معماری",'مکانیک', "دامپزشکی", "حقوق", "روانشناسی","مدیریت بازرگانی" ,"صنایع" ,"تربیت بدنی"]


    if StudentMajor not in allmajor:
        raise HTTPException(detail="رشته وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return "رشته وارد شده صحیح است"


