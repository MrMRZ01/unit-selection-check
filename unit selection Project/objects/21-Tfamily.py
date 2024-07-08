import re
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/")

def TF(TFamily):


    regexN20 = re.compile("^[آ-ی ]*$")

    findeN20 = regexN20.match(TFamily)


    if len(TFamily) > 15:
        raise HTTPException(detail="حروف فامیلی نباید بیش از 15 کاراکتر باشد.", status_code=status.HTTP_400_BAD_REQUEST)

    if len(TFamily) < 3:
        raise HTTPException(detail="فامیلی باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

    if not findeN20:
        raise HTTPException(detail="فاملی وارد شده نامعتبر است، لطفا فامیلی را به حروف فارسی وارد کنید.", status_code=status.HTTP_400_BAD_REQUEST)

    else:
        return ("فامیلی ثبت شد.")





