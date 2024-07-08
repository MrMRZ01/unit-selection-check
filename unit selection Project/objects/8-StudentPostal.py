from fastapi import FastAPI, HTTPException, status
import re

app = FastAPI()

@app.get("/home/{StudentPostal}")
def StudentPostal(StudentPostal):
    postal = StudentPostal
    len1 = len(postal)

    regexP = re.compile("^[0-9]*$")

    findeP = regexP.match(postal)

    if len1 >= 11 or len1 <= 9:
        raise HTTPException(detail="تعداد ارقام وارد شده نادرست است. کد پستی باید 10 رقم باشد", status_code=status.HTTP_400_BAD_REQUEST)
    if not findeP:
        raise HTTPException(detail="کدپستی وارد شده نادرست است، لطفا فقط از اعداد استفاده کنید.", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "کدپستی وارد شده صحیح است"