from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StudentInput(BaseModel):
    StudentNumber: int
    StudentName: str
    StudentBirth: str
    StudentCollege: str
    StudentState: str
    StudentSerial: str
    StudentCity: str
    StudentAddress: str
    StudentPostal: str
    StudentPhone: str
    StudentPhoneHome: str
    StudentField: str
    StudentMarital: str
    StudentNationalCode: str

@app.post("/home")
def validate_student(student: StudentInput


                     ):

    year = int(str(student.StudentNumber)[:3])
    constant_part = str(student.StudentNumber)[3:9]
    index = int(str(student.StudentNumber)[9:])
    len1 = int(len(str(student.StudentNumber)))

    year2 = int(str(student.StudentBirth)[:4])
    month = int(str(student.StudentBirth)[4:6])
    day = int(str(student.StudentBirth)[6:8])
    len2 = int(len(str(student.StudentBirth)))

    alpha3 = (str(student.StudentSerial)[:1])
    townum = int(str(student.StudentSerial)[2:4])
    sixnum = int(str(student.StudentSerial)[4:10])
    len3 = int(len(str(student.StudentSerial)))
    allalpha = ["آ", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د",
                "ذ", "ر", "ز", "ط", "ظ", "ع", "غ", "ک", "گ", "ل", "ض",
                "ص", "ف", "ق", "ن", "ی", "س", "ش", "ژ", "و", "م"]


    all_colleges = ["فنی و مهندسی", "علوم پایه", "شیمی", "اقتصاد", "ادبیات"]
    all_states = ["قم","مرکزی","تهران","لرستان",
                "همدان","کرمانشاه","ایلام","خوزستان","اصفهان"
                ,"گیلان","آذربایجان غربی","آذربایجان شرقی","آذربایجان","زنجان","قزوین","اردبیل",
                "چهارمحال","کهگیلویه و بویراحمد","کهگیلویه","چهارمحال و بختیاری","بوشهر","البرز","فارس",
                "سمنان","مازندران","گلستان","یزد","خراسان جنوبی","خراسان رضوی","خراسان شمالی",
                'کرمان',"هرمزگان",'سیستان',"سیستان و بلوچستان",'سایر']

# شهر--------------------------------------------------------------------

    city = student.StudentCity

# آدرس------------------------------------------------------------------

    address = student.StudentAddress
    len4 = int(len(address))

# کدپستی -------------------------------------------------------------

    postal = student.StudentPostal
    len5 = len(postal)

# شماره همراه----------------------------------------------------------

    phone = student.StudentPhone
    firsttow = str(phone[:2])
    len6 = int(len(str(phone)))

# شماره خانه----------------------------------------------------------

    phoneH = student.StudentPhoneHome
    len7 = int(len(str(phoneH)))
    code = str(phoneH)[:3]
    first = str(phoneH)[3:4]
    allcode = ["086", "021", '025', '041', '044', '045', '031', '026', '084', '077',
               '028', '071', '054', '023', '024', '058', '061', '051', '056', '038',
               '087', '034', '083', '013', '017', '074', '066', '011', '076', '081', '035']
    allfirst = ['3', '4', '5', '8']

# رشته تحصیلی---------------------------------------------------------------------------

    allfield = ["برق", "کامپیوتر",
                "عمران", "معماری", 'مکانیک']

# وضعیت تاهل-----------------------------------------------------------------------

    maritalstatus = ["متاهل", "مجرد"]

# برای کدملی---------------------------------------------------------------------

    code1 = student.StudentNationalCode
    l = len(code1)
    sum = 0







    errors = []





# برای شماره دانشجویی --------------------------------------------------

    if len1 < 11 or len1 > 11:
        errors.append("شماره دانشجویی باید 11 رقم باشد")
    if constant_part != "114150":
        errors.append("قسمت ثابت نادرست است")
    if year >= 403 or year <= 399:
        errors.append(" سال وارد شده در قسمت اول شماره دانشجویی نادرست است")
    if index < 1 or index > 99:
        errors.append("اندیس نادرست است")


# برای نام--------------------------------------------------------------

    if not student.StudentName.isalpha():
        errors.append ("نام باید فقط شامل حروف فارسی باشد.")
    if len(student.StudentName) > 15:
        errors.append("نام نباید بیشتر از 15 حرف باشد.")
    for char in student.StudentName:
        if not char.isalpha():
            errors.append("نام نباید حاوی عدد یا علامت خاص باشد.")

# برای تاریخ تولد-------------------------------------------------------

    if len2 >= 9 or len2 <= 7:
        errors.append("تعداد ارقام وارد شده نادرست است")
    if year2 >= 1500 or year2 <= 1250:
        errors.append(" سال وارد شده نادرست است")
    if month >= 13 or month <= 1:
        errors.append("ماه وارد شده نادرست است")
    if day >= 32 or day <= 0:
        errors.append("روز وارد شده نادرست است")

# برای سریال شناسنامه----------------------------------------------------------------

    if len3 >= 10 or len3 <= 8:
        errors.append("تعداد کاراکتر های وارد شده سریال نادرست است")
    if alpha3 not in allalpha:
        errors.append("حرف فارسی وارد شده در سریال نادرست است")
    if not isinstance(townum, int):
        errors.append("بخش دو رقمی سریال حتما باید عدد باشد")
    if not isinstance(sixnum, int):
        errors.append("بخش شش رقمی سریال شناسنامه نیز حتما باید عدد باشد")


# برای دانشکده---------------------------------------------------------------------------------

    if student.StudentCollege not in all_colleges:
        errors.append("دانشکده وارد شده نادرست است")

# برای استان-----------------------------------------------------------------------------------

    if student.StudentState not in all_states:
        errors.append("استان وارد شده نادرست است")

# برای شهر ----------------------------------------------------------------------------------

    if not city.isalpha():
        errors.append("لطفا نام شهر را به فارسی وارد کنید و از اعداد استفاده نکنید")

# برای آدرس------------------------------------------------------------------------------------

    if len4 >= 101:
        errors.append("تعداد کاراکتر های مجاز استفاده 100 عدد می باشد")
    if address is int:
        errors.append("لطفا آدرس را به فارسی وارد کنید و صرفا از اعدد استفاده نکنید")

# برای کدپستی-------------------------------------------------------------------------------------

    if len5 >= 11 or len5 <= 9:
        errors.append("تعداد ارقام وارد شده نادرست است. کد پستی باید 10 رقم باشد")

# برای شماره همراه------------------------------------------------------------------------------------

    if firsttow != "09":
        errors.append("شماره وارد شده مطابق استاندارد شماره های کشور جمهوری اسلامی ایران نمی باشد")
    if len6 >= 12 or len6 <= 10:
        errors.append("شماره وارد شده نادرست است. ارقام وارده باید 11 رقم باشد")

# شماره خانه-----------------------------------------------------------------------------------------

    if code not in allcode:
        errors.append("کد شهرستان وارد شده نادرست است")
    if first not in allfirst:
        errors.append("رقم اول بعد از کد شهرستان نادرست است")
    if len1 >= 12 or len1 <= 10:
        errors.append("ارقام وارده باید 11 رقم باشد")

# برای رشته تحصیلی------------------------------------------------------------------------------------

    if student.StudentField not in allfield:
        errors.append("رشته وارد شده نادرست است")

# برای وضعیت تاهل--------------------------------------------------------------------------------

    if student.StudentMarital not in maritalstatus:
        errors.append("لطفا یکی از دو گزینه مجرد و یا متاهل را وارد کنید")

# برای کدملی----------------------------------------------------------------------------

    for i in range(0, l - 1):
        c = ord(code1[i])
        c -= 48
        sum = sum + c * (l - i)
    r = sum % 11
    c = ord(code1[l - 1])
    c -= 48
    if r > 2:
        r = 11 - r
    if r != c:
        errors.append("کدملی وارد شده نامعتبر است")



    if errors:
        return {"errors": errors}
    for error in errors:
        return {"error": error}
    return {"message": "ورودی‌ها صحیح است"}

