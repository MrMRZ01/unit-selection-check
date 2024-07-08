from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get('/home/{StudentNumber}')
def StudentNumber(StudentNumber):
    year = int(str(StudentNumber)[:3])
    constant_part = str(StudentNumber)[3:9]
    index = int(str(StudentNumber)[9:])
    len1 = int(len(str(StudentNumber)))


    if len1 < 11 or len1 > 11:
        raise HTTPException(detail="شماره دانشجویی باید 11 رقم باشد", status_code=status.HTTP_400_BAD_REQUEST)
    if constant_part != "114150":
        raise HTTPException(detail="قسمت ثابت نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if year >= 403 or year <= 399:
        raise HTTPException(detail=" سال وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if index < 1 or index > 99:
        raise HTTPException(detail="اندیس نادرست است", status_code=status.HTTP_400_BAD_REQUEST)

    else:
        return f"سال: {year+1000}, قسمت ثابت: {constant_part}, اندیس: {index}"

