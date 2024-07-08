import re
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/")

def CN(CName):


    regexN100 = re.compile("^[آ-ی 1-4]*$")

    findeN100 = regexN100.match(CName)


    if len(CName) > 20:
        raise HTTPException(detail="حروف نام درس نباید بیش از 20 کاراکتر باشد.", status_code=status.HTTP_400_BAD_REQUEST)

    if len(CName) < 3:
        raise HTTPException(detail="نام درس باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

    if not findeN100:
        raise HTTPException(detail="نام درس وارد شده نامعتبر است، لطفا نام را به حروف فارسی وارد کنید.", status_code=status.HTTP_400_BAD_REQUEST)

    else:
        return ("نام درس ثبت شد.")





