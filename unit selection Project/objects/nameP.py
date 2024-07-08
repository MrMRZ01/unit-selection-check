import re
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def StudentName(StudentName):

    if len(StudentName) > 15:
        return ("حروف نام نباید بیش از 15 کاراکتر باشد.")

    if len(StudentName) < 3:
        return ("نام باید حداقل 3 حرف داشته باشد.")

    if re.match("^[ آ-ی]+$", StudentName):
        return ("نام ذخیره شد")

    else:
        return ("نام وارد شده نامعتبر است، لطفا نام با حروف فارسی وارد کنید.")





