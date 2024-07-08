from fastapi import FastAPI, HTTPException, status
import re

app = FastAPI()

@app.get("/home/{StudentCity}")
def StudentCity(StudentCity):
    city = StudentCity

    regex = re.compile("^[آ-ی]*$")

    findere = regex.match(city)



    # if city == int:
    if not findere:
        raise HTTPException(detail="لطفا نام شهر را به فارسی وارد کنید و از اعداد استفاده نکنید", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "شهر وارد شده درست است"

