from fastapi import FastAPI, HTTPException, status
import re

app = FastAPI()

@app.get("/home/{StudentAddress}")
def StudentAddress(StudentAddress):
    address = StudentAddress
    len1 = int(len(address))

    regexA = re.compile("^[ 0-9آ-ی]*$")

    findeA = regexA.match(address)

    if len1 >= 101:
        raise HTTPException(detail="تعداد کاراکتر های مجاز استفاده 100 عدد می باشد", status_code=status.HTTP_400_BAD_REQUEST)
    if not findeA:
        raise HTTPException(detail="لطفا آدرس را به فارسی وارد کنید و صرفا از اعدد استفاده نکنید", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "آدرس وارد شده صحیح است"