from fastapi import FastAPI, HTTPException, status
import re
app = FastAPI()

@app.get('/home/CID}')
def CI(CID):

    len300 = len(CID)

    regexcid = re.compile("^[0-9]*$")
    findcid = regexcid.match(CID)

    if len300 != 5:
        raise HTTPException(detail="شماره درس باید 5 رقم باشد.", status_code=status.HTTP_400_BAD_REQUEST)
    if not findcid:
        raise HTTPException(detail="لطفا برای شماره درس فقط از اعداد استفاده نمایید.", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "شماره درس ثبت شد."