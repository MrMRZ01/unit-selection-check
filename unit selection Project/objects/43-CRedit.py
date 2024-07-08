from fastapi import FastAPI, HTTPException, status
import re
app = FastAPI()

@app.get('/home/Credit}')
def CR(Credit):

    regexcr = re.compile("^[1-4]$")
    findcr = regexcr.match(Credit)

    if not findcr:
        raise HTTPException(detail="لطفا برای واحد درس فقط از اعداد یک تا چهار استفاده نمایید.", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return "واحد درس ثبت شد."