from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get('/home/{TBirth}')
def TB(TBirth):
    year1 = int(str(TBirth)[:4])
    month1 = int(str(TBirth)[4:6])
    day1 = int(str(TBirth)[6:8])
    len10 = int(len(str(TBirth)))

    if len10 >= 9 or len10 <= 7:
        raise HTTPException(detail="تعداد ارقام وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if year1 >= 1403 or year1 <= 1300:
        raise HTTPException(detail=" سال وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if month1 >= 13 or month1 <= 1:
        raise HTTPException(detail="ماه وارد شدن نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if day1 >= 32 or day1 <= 0:
        raise HTTPException(detail="روز وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "تاریخ تولد صحیح است"

