from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/home/{TNationalCode}")
def TNC(TNationalCode):
    code1 = TNationalCode
    l1 = len(code1)
    sum1 = 0
    for i in range(0, l1 - 1):
        c = ord(code1[i])
        c -= 48
        sum1 = sum1 + c * (l1 - i)
    r = sum1 % 11
    c = ord(code1[l1 - 1])
    c -= 48
    if r > 2:
        r = 11 - r
    if r != c:
        raise HTTPException(detail="کدملی وارد شده نامعتبر است", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "کدملی وارد شده صحیح است"