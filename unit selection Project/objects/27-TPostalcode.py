from fastapi import FastAPI, HTTPException, status
import re

app = FastAPI()

@app.get("/home/{TPostal}")
def TP(TPostal):
    postal1 = TPostal
    len10 = len(postal1)

    regexP1 = re.compile("^[0-9]*$")

    findeP1 = regexP1.match(postal1)

    if len10 >= 11 or len10 <= 9:
        raise HTTPException(detail="تعداد ارقام وارد شده نادرست است. کد پستی باید 10 رقم باشد", status_code=status.HTTP_400_BAD_REQUEST)
    if not findeP1:
        raise HTTPException(detail="کدپستی وارد شده نادرست است، لطفا فقط از اعداد استفاده کنید.", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "کدپستی وارد شده صحیح است"