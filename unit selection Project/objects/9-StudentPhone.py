from fastapi import FastAPI, HTTPException, status
import re

app = FastAPI()

@app.get("/home/{StudentPhone}")
def StudentPone(StudentPhone):
    phone = StudentPhone
    firsttow = str(phone[:2])
    len1 = int(len(str(phone)))

    regexP1 = re.compile("^[0-9]*$")

    findeP1 = regexP1.match(firsttow)


    if firsttow != "09":
        raise HTTPException(detail="شماره وارد شده مطابق استاندارد شماره های کشور جمهوری اسلامی ایران نمی باشد", status_code=status.HTTP_400_BAD_REQUEST)
    if len1 >= 12 or len1 <= 10:
        raise HTTPException(detail="ارقام وارده باید 11 رقم باشد", status_code=status.HTTP_400_BAD_REQUEST)
    if not findeP1:
        raise HTTPException(detail="شماره وارد شده نادرست است لطفا فقط از اعداد استفاده کنید", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "شماره وارد شده صحیح است"