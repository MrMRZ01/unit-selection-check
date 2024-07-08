from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/home/{StudentMarital}")
def StudentMarital(StudentMarital: str):
    maritalstatus = ["متاهل","مجرد"]



    if StudentMarital not in maritalstatus:
        raise HTTPException(detail="لطفا یکی از دو گزینه مجرد و یا متاهل را وارد کنید", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return "وضعیت وارد شد"


