from fastapi import FastAPI, HTTPException, status
import re
app = FastAPI()

@app.get("/home/{StudentSerial}")
def StudentSerial(StudentSerial):
    alpha = (str(StudentSerial)[:1])
    townum = int(str(StudentSerial)[2:4])
    sixnum = int(str(StudentSerial)[4:10])
    len1 = int(len(str(StudentSerial)))
    # allalpha = ["آ", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د",
    #             "ذ", "ر", "ز", "ط", "ظ", "ع", "غ", "ک", "گ", "ل", "ض",
    #             "ص", "ف", "ق", "ن", "ی", "س", "ش", "ژ", "و", "م"]

    allalpha = alpha

    regexS = re.compile("^[آ-ی]$")

    findeS = regexS.match(allalpha)

    if len1 >= 10 or len1 <= 8:
        raise HTTPException(detail="تعداد کاراکتر های وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if not findeS:
        raise HTTPException(detail="حرف فارسی وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
    if not isinstance(townum, int):
        raise HTTPException(detail="بخش دو رقمی حتما باید عدد باشد", status_code=status.HTTP_400_BAD_REQUEST)
    if not isinstance(sixnum, int):
        raise HTTPException(detail="بخش شش رقمی نیز حتما باید عدد باشد", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "شماره شناسنامه وارد شده صحیح است"














