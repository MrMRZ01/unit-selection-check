import re
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/")

def StudentName(StudentName):


    regexN1 = re.compile("^[آ-ی ]*$")

    findeN1 = regexN1.match(StudentName)


    if len(StudentName) > 10:
        raise HTTPException(detail="حروف نام نباید بیش از 10 کاراکتر باشد.", status_code=status.HTTP_400_BAD_REQUEST)

    if len(StudentName) < 3:
        raise HTTPException(detail="نام باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

    if not findeN1:
        raise HTTPException(detail="نام وارد شده نامعتبر است، لطفا نام را به حروف فارسی وارد کنید.", status_code=status.HTTP_400_BAD_REQUEST)

    else:
        return ("نام ثبت شد.")





