from fastapi import FastAPI, HTTPException, status
import re

app = FastAPI()

@app.get("/home/{TPhone}")
def TPH(TPhone):
    phone1 = TPhone
    firsttow1 = str(phone1[:2])
    len10 = int(len(str(phone1)))

    regexP10 = re.compile("^[0-9]*$")

    findeP10 = regexP10.match(firsttow1)


    if firsttow1 != "09":
        raise HTTPException(detail="شماره وارد شده مطابق استاندارد شماره های کشور جمهوری اسلامی ایران نمی باشد", status_code=status.HTTP_400_BAD_REQUEST)
    if len10 >= 12 or len10 <= 10:
        raise HTTPException(detail="ارقام وارده باید 11 رقم باشد", status_code=status.HTTP_400_BAD_REQUEST)
    if not findeP10:
        raise HTTPException(detail="شماره وارد شده نادرست است لطفا فقط از اعداد استفاده کنید", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "شماره وارد شده صحیح است"