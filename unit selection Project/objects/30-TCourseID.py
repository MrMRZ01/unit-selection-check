from fastapi import FastAPI, HTTPException, status
import re
app = FastAPI()

@app.get('/home/TCID}')
def TCI(TCID):

    len31 = len(TCID)

    regextcid = re.compile("^[0-9]*$")
    findtcid = regextcid.match(TCID)

    if len31 != 5:
        raise HTTPException(detail="شماره درس باید 5 رقم باشد.", status_code=status.HTTP_400_BAD_REQUEST)
    if not findtcid:
        raise HTTPException(detail="لطفا برای شماره درس فقط از اعداد استفاده نمایید.", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "شماره درس ثبت شد."