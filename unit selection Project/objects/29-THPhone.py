from fastapi import FastAPI, HTTPException, status
import re

app = FastAPI()

@app.get("/home/{THPhone}")
def THP(THPhone):
    phoneH1 = THPhone
    len1 = int(len(str(phoneH1)))
    code1 = str(phoneH1)[:3]
    first1 = str(phoneH1)[3:4]
    allcode1 = ["086","021",'025','041','044','045','031','026','084','077',
               '028','071','054','023','024','058','061','051','056','038',
               '087','034','083','013','017','074','066','011','076','081','035']
    allfirst = ['3','4','5','8']

    regexH1 = re.compile("^[0-9]*$")

    findeH1 = regexH1.match(phoneH1)


    if code1 not in allcode1:
        raise HTTPException(detail="کد شهرستان وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if first1 not in allfirst:
        raise HTTPException(detail="رقم اول بعد از کد شهرستان نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if len1 >= 12 or len1 <= 10:
        raise HTTPException(detail="ارقام وارده باید 11 رقم باشد", status_code=status.HTTP_400_BAD_REQUEST)
    if not findeH1:
        raise HTTPException(detail="شماره وارد شده نادرست است لطفا فقط از اعداد استفاده کنید.", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "شماره وارد شده صحیح است"