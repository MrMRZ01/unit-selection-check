from fastapi import FastAPI, HTTPException, status
import re
app = FastAPI()

@app.get('/home/{TID}')
def TI(TID):

    len30 = len(TID)

    regextid = re.compile("^[0-9]*$")
    findtid = regextid.match(TID)

    if len30 != 6:
        raise HTTPException(detail="شماره استادی باید 6 رقم باشد.", status_code=status.HTTP_400_BAD_REQUEST)
    if not findtid:
        raise HTTPException(detail="لطفا برای شماره استادی فقط از اعداد استفاده نمایید.", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "شماره استادی ثبت شد."