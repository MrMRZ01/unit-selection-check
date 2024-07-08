from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get('/home/{StudentBirth}')
def StudentBirth(StudentBirth):
    year = int(str(StudentBirth)[:4])
    month = int(str(StudentBirth)[4:6])
    day = int(str(StudentBirth)[6:8])
    len1 = int(len(str(StudentBirth)))

    if len1 >= 9 or len1 <= 7:
        raise HTTPException(detail="تعداد ارقام وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if year >= 1403 or year <= 1300:
        raise HTTPException(detail=" سال وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if month >= 13 or month <= 1:
        raise HTTPException(detail="ماه وارد شدن نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if day >= 32 or day <= 0:
        raise HTTPException(detail="روز وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "تاریخ تولد صحیح است"

