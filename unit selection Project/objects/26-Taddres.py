from fastapi import FastAPI, HTTPException, status
import re

app = FastAPI()

@app.get("/home/{TAddress}")
def TA(TAddress):
    address = TAddress
    len10 = int(len(address))

    regexA1 = re.compile("^[ 0-9آ-ی]*$")

    findeA1 = regexA1.match(address)

    if len10 >= 101:
        raise HTTPException(detail="تعداد کاراکتر های مجاز استفاده 100 عدد می باشد", status_code=status.HTTP_400_BAD_REQUEST)
    if not findeA1:
        raise HTTPException(detail="لطفا آدرس را به فارسی وارد کنید و صرفا از اعدد استفاده نکنید", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "آدرس وارد شده صحیح است"