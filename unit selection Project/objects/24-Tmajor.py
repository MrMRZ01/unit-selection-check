from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/home/{TMajor}")
def TM(TMajor: str):
    allmajor1 = ["برق","کامپیوتر",
                  "عمران","معماری",'مکانیک', "دامپزشکی", "حقوق", "روانشناسی","مدیریت بازرگانی" ,"صنایع" ,"تربیت بدنی"]


    if TMajor not in allmajor1:
        raise HTTPException(detail="رشته وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return "رشته وارد شده صحیح است"


