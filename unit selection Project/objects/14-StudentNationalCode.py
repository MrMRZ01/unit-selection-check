from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/home/{StudentNationalCode}")
def StudentNationalCode(StudentNationalCode):
    code = StudentNationalCode
    l = len(code)
    sum = 0
    for i in range(0, l - 1):
        c = ord(code[i])
        c -= 48
        sum = sum + c * (l - i)
    r = sum % 11
    c = ord(code[l - 1])
    c -= 48
    if r > 2:
        r = 11 - r
    if r != c:
        raise HTTPException(detail="کدملی وارد شده نامعتبر است", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "کدملی وارد شده صحیح است"