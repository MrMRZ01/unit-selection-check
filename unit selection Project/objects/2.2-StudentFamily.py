import re
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/")

def StudentFamily(StudentFamily):


    regexN2 = re.compile("^[آ-ی ]*$")

    findeN2 = regexN2.match(StudentFamily)


    if len(StudentFamily) > 15:
        raise HTTPException(detail="حروف فامیلی نباید بیش از 15 کاراکتر باشد.", status_code=status.HTTP_400_BAD_REQUEST)

    if len(StudentFamily) < 3:
        raise HTTPException(detail="فامیلی باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

    if not findeN2:
        raise HTTPException(detail="فاملی وارد شده نامعتبر است، لطفا فامیلی را به حروف فارسی وارد کنید.", status_code=status.HTTP_400_BAD_REQUEST)

    else:
        return ("فامیلی ثبت شد.")





