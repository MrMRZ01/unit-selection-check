from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/home/{StudentState}")
def StudentState(StudentState):
    state = str(StudentState)
    allstate = ["قم","مرکزی","تهران","لرستان",
                "همدان","کرمانشاه","ایلام","خوزستان","اصفهان"
                ,"گیلان","آذربایجان غربی","آذربایجان شرقی","آذربایجان","زنجان","قزوین","اردبیل",
                "چهارمحال","کهگیلویه و بویراحمد","کهگیلویه","چهارمحال و بختیاری","بوشهر","البرز","فارس",
                "سمنان","مازندران","گلستان","یزد","خراسان جنوبی","خراسان رضوی","خراسان شمالی",
                'کرمان',"هرمزگان",'سیستان',"سیستان و بلوچستان",'سایر']

    if state not in allstate:
        raise HTTPException(detail="استان وارد شده نادرست است; میتوانید کلمه سایر را وارد کنید", status_code=status.HTTP_404_NOT_FOUND)
    else:
        return "استان وارد شده صحیح است"


