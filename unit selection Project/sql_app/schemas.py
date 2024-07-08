from pydantic import BaseModel, validator
import re
from fastapi import HTTPException, status
from .database import SessionLocal
from ..sql_app import crud



db = SessionLocal()



class Course(BaseModel):
    cid: str
    cname: str
    department: str
    credit: int #تعداد واحد درس

    @validator("cid")
    def CI(CID: str):

        len300 = len(CID)

        regexcid = re.compile("^[0-9]*$")
        findcid = regexcid.match(CID)

        if len300 != 5:
            raise HTTPException(detail="شماره درس باید 5 رقم باشد.", status_code=status.HTTP_400_BAD_REQUEST)
        if not findcid:
            raise HTTPException(detail="لطفا برای شماره درس فقط از اعداد استفاده نمایید.",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "شماره درس ثبت شد."

    @validator("cname")
    def CN(CName):
        CNamee = str(CName)
        regexN100 = re.compile("^[آ-ی 1-4]*$")

        findeN100 = regexN100.match(CNamee)

        if len(CNamee) > 20:
            raise HTTPException(detail="حروف نام درس نباید بیش از 20 کاراکتر باشد.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        if len(CNamee) < 3:
            raise HTTPException(detail="نام درس باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

        if not findeN100:
            raise HTTPException(detail="نام درس وارد شده نامعتبر است، لطفا نام را به حروف فارسی وارد کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return ("نام درس ثبت شد.")

    @validator("department")
    def CD(CDepartment: str):
        allDepartment1 = ["فنی و مهندسی", "علوم پایه",
                          "شیمی", "اقتصاد", 'ادبیات', "دامپزشکی"]

        if CDepartment not in allDepartment1:
            raise HTTPException(detail="دانشکده وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "دانشکده وارد شده ثبت شد."

    @validator("credit")
    def CR(credit):
        Creditt = str(credit)
        regexcr = re.compile("^[1-4]$")
        findcr = regexcr.match(Creditt)

        if not findcr:
            raise HTTPException(detail="لطفا برای واحد درس فقط از اعداد یک تا چهار استفاده نمایید.",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "واحد درس ثبت شد."



class Teacher(BaseModel):
    Tid: str #کداستادی
    Tname: str
    TLname: str #فامیلی
    Tmajor: str #رشته تحصیلی
    Tbirth: str #تاریخ تولد
    Tborn: str #محل تولد
    Taddress: str
    Tpostal: str #کدپستی
    Tphone: str
    THphone: str #تلفن ثابت
    Tcuorseid: str #کد دروس ارایه شده
    TNid: str #کدملی استاد
    Tdepartment: str #دانشکده

    @validator("Tname")
    def TN(Tname):
        Tnamee = str(Tname)
        regexN10 = re.compile("^[آ-ی ]*$")

        findeN10 = regexN10.match(Tnamee)

        if len(Tnamee) > 10:
            raise HTTPException(detail="حروف نام نباید بیش از 10 کاراکتر باشد.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        if len(Tnamee) < 3:
            raise HTTPException(detail="نام باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

        if not findeN10:
            raise HTTPException(detail="نام وارد شده نامعتبر است، لطفا نام را به حروف فارسی وارد کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return "نام ثبت شد."

    @validator("TLname")
    def TF(TLname):
        TLnamee = str(TLname)
        regexN20 = re.compile("^[آ-ی ]*$")

        findeN20 = regexN20.match(TLnamee)

        if len(TLnamee) > 15:
            raise HTTPException(detail="حروف فامیلی نباید بیش از 15 کاراکتر باشد.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        if len(TLnamee) < 3:
            raise HTTPException(detail="فامیلی باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

        if not findeN20:
            raise HTTPException(detail="فاملی وارد شده نامعتبر است، لطفا فامیلی را به حروف فارسی وارد کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return ("فامیلی ثبت شد.")

    @validator("TNid")
    def TNC(TNid):
        code1 = str(TNid)
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

    @validator("Tdepartment")
    def TD(Tdepartment: str):
        allDepartment1 = ["فنی و مهندسی", "علوم پایه",
                          "شیمی", "اقتصاد", 'ادبیات', "دامپزشکی"]

        if Tdepartment not in allDepartment1:
            raise HTTPException(detail="دانشکده وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "دانشکده وارد شده ثبت شد."

    @validator("Tmajor")
    def TM(Tmajor: str):
        allmajor1 = ["برق", "کامپیوتر",
                     "عمران", "معماری", 'مکانیک', "دامپزشکی", "حقوق", "روانشناسی", "مدیریت بازرگانی", "صنایع",
                     "تربیت بدنی"]

        if Tmajor not in allmajor1:
            raise HTTPException(detail="رشته وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "رشته وارد شده صحیح است"

    @validator("Tbirth")
    def TB(Tbirth):
        year1 = int(str(Tbirth)[:4])
        month1 = int(str(Tbirth)[4:6])
        day1 = int(str(Tbirth)[6:8])
        len10 = int(len(str(Tbirth)))

        if len10 >= 9 or len10 <= 7:
            raise HTTPException(detail="تعداد ارقام وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if year1 >= 1403 or year1 <= 1300:
            raise HTTPException(detail=" سال وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if month1 >= 13 or month1 <= 1:
            raise HTTPException(detail="ماه وارد شدن نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if day1 >= 32 or day1 <= 0:
            raise HTTPException(detail="روز وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "تاریخ تولد صحیح است"

    @validator("Taddress")
    def TA(Taddress):
        address = str(Taddress)
        len10 = int(len(address))

        regexA1 = re.compile("^[ 0-9آ-ی]*$")

        findeA1 = regexA1.match(address)

        if len10 >= 101:
            raise HTTPException(detail="تعداد کاراکتر های مجاز استفاده 100 عدد می باشد",
                                status_code=status.HTTP_400_BAD_REQUEST)
        if not findeA1:
            raise HTTPException(detail="لطفا آدرس را به فارسی وارد کنید و صرفا از اعدد استفاده نکنید",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "آدرس وارد شده صحیح است"

    @validator("Tpostal")
    def TP(Tpostal):
        postal1 = str(Tpostal)
        len10 = len(postal1)

        regexP1 = re.compile("^[0-9]*$")

        findeP1 = regexP1.match(postal1)

        if len10 >= 11 or len10 <= 9:
            raise HTTPException(detail="تعداد ارقام وارد شده نادرست است. کد پستی باید 10 رقم باشد",
                                status_code=status.HTTP_400_BAD_REQUEST)
        if not findeP1:
            raise HTTPException(detail="کدپستی وارد شده نادرست است، لطفا فقط از اعداد استفاده کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "کدپستی وارد شده صحیح است"

    @validator("Tphone")
    def TPH(Tphone):
        phone1 = Tphone
        firsttow1 = str(phone1[:2])
        len10 = int(len(str(phone1)))

        regexP10 = re.compile("^[0-9]*$")

        findeP10 = regexP10.match(firsttow1)

        if firsttow1 != "09":
            raise HTTPException(detail="شماره وارد شده مطابق استاندارد شماره های کشور جمهوری اسلامی ایران نمی باشد",
                                status_code=status.HTTP_400_BAD_REQUEST)
        if len10 >= 12 or len10 <= 10:
            raise HTTPException(detail="ارقام وارده باید 11 رقم باشد", status_code=status.HTTP_400_BAD_REQUEST)
        if not findeP10:
            raise HTTPException(detail="شماره وارد شده نادرست است لطفا فقط از اعداد استفاده کنید",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "شماره وارد شده صحیح است"

    @validator("THphone")
    def THP(THphone):
        phoneH1 = str(THphone)
        len1 = int(len(str(phoneH1)))
        code1 = str(phoneH1)[:3]
        first1 = str(phoneH1)[3:4]
        allcode1 = ["086", "021", '025', '041', '044', '045', '031', '026', '084', '077',
                    '028', '071', '054', '023', '024', '058', '061', '051', '056', '038',
                    '087', '034', '083', '013', '017', '074', '066', '011', '076', '081', '035']
        allfirst = ['3', '4', '5', '8']

        regexH1 = re.compile("^[0-9]*$")

        findeH1 = regexH1.match(phoneH1)

        if code1 not in allcode1:
            raise HTTPException(detail="کد شهرستان وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if first1 not in allfirst:
            raise HTTPException(detail="رقم اول بعد از کد شهرستان نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if len1 >= 12 or len1 <= 10:
            raise HTTPException(detail="ارقام وارده باید 11 رقم باشد", status_code=status.HTTP_400_BAD_REQUEST)
        if not findeH1:
            raise HTTPException(detail="شماره وارد شده نادرست است لطفا فقط از اعداد استفاده کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "شماره وارد شده صحیح است"

    # @validator("Tcourseid")
    # def TCI(Tcourseid):
    #
    #     len31 = len(Tcourseid)
    #
    #     regextcid = re.compile("^[0-9]*$")
    #     findtcid = regextcid.match(Tcourseid)
    #
    #     if len31 != 5:
    #         raise HTTPException(detail="شماره درس باید 5 رقم باشد.", status_code=status.HTTP_400_BAD_REQUEST)
    #     if not findtcid:
    #         raise HTTPException(detail="لطفا برای شماره درس فقط از اعداد استفاده نمایید.",
    #                             status_code=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return "شماره درس ثبت شد."

    @validator("Tid")
    def TI(Tid):
        Tidd = str(Tid)
        len30 = len(Tidd)

        regextid = re.compile("^[0-9]*$")
        findtid = regextid.match(Tidd)

        if len30 != 6:
            raise HTTPException(detail="شماره استادی باید 6 رقم باشد.", status_code=status.HTTP_400_BAD_REQUEST)
        if not findtid:
            raise HTTPException(detail="لطفا برای شماره استادی فقط از اعداد استفاده نمایید.",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "شماره استادی ثبت شد."

    @validator("Tcuorseid")
    def TCID(cls, value):
        try:
            Courses = value.split(",")
            for course in Courses:
                a = int(course)
        except:
            raise ValueError("Courses id must separate by ,")

        for course in Courses:
            course =  crud.get_Course(db, int(course))
            if course is None:
                raise ValueError("Courses id is not correct!")

        return "کد دروس ثبت شد"


class Student(BaseModel):
    Sid: str
    Sname: str
    SLname: str  # فامیلی
    Sfather: str #نام پدر
    Sids: str #سریال شناسنامه
    Smajor: str  # رشته تحصیلی
    Sbirth: str  # تاریخ تولد
    Sborn: str  # محل تولد
    Saddress: str
    Spostal: str  # کدپستی
    Sphone: str
    SHphone: str  # تلفن ثابت
    # Scuorseid: str  # کد دروس اخذ شده
    SNid: str  # کدملی دانشجو
    Smarried: str #وضعیت تاهل
    Sdepartment: str  # دانشکده
    SLid: str #کد اساتید
    course_numbers: str

    SCourseIDs: list[Course] = []
    SLIDs: list[Teacher] = []

    @validator("Sid")
    def SID(Sid):
        year = int(str(Sid)[:3])
        constant_part = str(Sid)[3:9]
        index = int(str(Sid)[9:])
        len1 = int(len(str(Sid)))

        if len1 < 11 or len1 > 11:
            raise HTTPException(detail="شماره دانشجویی باید 11 رقم باشد", status_code=status.HTTP_400_BAD_REQUEST)
        if constant_part != "114150":
            raise HTTPException(detail="قسمت ثابت نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if year >= 403 or year <= 399:
            raise HTTPException(detail=" سال وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if index < 1 or index > 99:
            raise HTTPException(detail="اندیس نادرست است", status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return f"سال: {year + 1000}, قسمت ثابت: {constant_part}, اندیس: {index}"
    @validator("SLname")
    def SL(SLname):
        SLnamee = str(SLname)
        regexN2 = re.compile("^[آ-ی ]*$")

        findeN2 = regexN2.match(SLnamee)

        if len(SLnamee) > 15:
            raise HTTPException(detail="حروف فامیلی نباید بیش از 15 کاراکتر باشد.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        if len(SLnamee) < 3:
            raise HTTPException(detail="فامیلی باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

        if not findeN2:
            raise HTTPException(detail="فاملی وارد شده نامعتبر است، لطفا فامیلی را به حروف فارسی وارد کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return ("فامیلی ثبت شد.")
    @validator("Sname")
    def SN(Sname):
        Snamee = str(Sname)
        regexN1 = re.compile("^[آ-ی ]*$")

        findeN1 = regexN1.match(Snamee)

        if len(Snamee) > 10:
            raise HTTPException(detail="حروف نام نباید بیش از 10 کاراکتر باشد.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        if len(Snamee) < 3:
            raise HTTPException(detail="نام باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

        if not findeN1:
            raise HTTPException(detail="نام وارد شده نامعتبر است، لطفا نام را به حروف فارسی وارد کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return ("نام ثبت شد.")
    @validator("Sbirth")
    def SBirth(Sbirth):
        year = int(str(Sbirth)[:4])
        month = int(str(Sbirth)[4:6])
        day = int(str(Sbirth)[6:8])
        len1 = int(len(str(Sbirth)))

        if len1 >= 9 or len1 <= 7:
            raise HTTPException(detail="تعداد ارقام وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if year >= 1403 or year <= 1300:
            raise HTTPException(detail=" سال وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if month >= 13 or month <= 1:
            raise HTTPException(detail="ماه وارد شدن نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if day >= 32 or day <= 0:
            raise HTTPException(detail="روز وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "تاریخ تولد صحیح است"
    @validator("Sids")
    def SIDS(Sids):
        alpha = (str(Sids)[:1])
        townum = int(str(Sids)[2:4])
        sixnum = int(str(Sids)[4:10])
        len1 = int(len(str(Sids)))
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
    @validator("Sborn")
    def SB(Sborn):
        state = str(Sborn)
        allstate = ["قم", "مرکزی", "تهران", "لرستان","خرم آباد"
                    "همدان", "کرمانشاه", "ایلام", "خوزستان", "اصفهان"
            , "گیلان", "آذربایجان غربی", "آذربایجان شرقی", "آذربایجان", "زنجان", "قزوین", "اردبیل",
                    "چهارمحال", "کهگیلویه و بویراحمد", "کهگیلویه", "چهارمحال و بختیاری", "بوشهر", "البرز", "فارس",
                    "سمنان", "مازندران", "گلستان", "یزد", "خراسان جنوبی", "خراسان رضوی", "خراسان شمالی",
                    'کرمان', "هرمزگان", 'سیستان', "سیستان و بلوچستان", 'سایر']

        if state not in allstate:
            raise HTTPException(detail="استان وارد شده نادرست است; میتوانید کلمه سایر را وارد کنید",
                                status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "استان وارد شده صحیح است"
    @validator("Saddress")
    def SA(Saddress):
        address = str(Saddress)
        len1 = int(len(address))

        regexA = re.compile("^[ 0-9آ-ی]*$")

        findeA = regexA.match(address)

        if len1 >= 101:
            raise HTTPException(detail="تعداد کاراکتر های مجاز استفاده 100 عدد می باشد",
                                status_code=status.HTTP_400_BAD_REQUEST)
        if not findeA:
            raise HTTPException(detail="لطفا آدرس را به فارسی وارد کنید و صرفا از اعدد استفاده نکنید",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "آدرس وارد شده صحیح است"
    @validator("Spostal")
    def SPostal(Spostal):
        postal = str(Spostal)
        len1 = len(postal)

        regexP = re.compile("^[0-9]*$")

        findeP = regexP.match(postal)

        if len1 >= 11 or len1 <= 9:
            raise HTTPException(detail="تعداد ارقام وارد شده نادرست است. کد پستی باید 10 رقم باشد",
                                status_code=status.HTTP_400_BAD_REQUEST)
        if not findeP:
            raise HTTPException(detail="کدپستی وارد شده نادرست است، لطفا فقط از اعداد استفاده کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "کدپستی وارد شده صحیح است"
    @validator("Sphone")
    def SPhone(Sphone):
        phone = Sphone
        firsttow = str(phone[:2])
        len1 = int(len(str(phone)))

        regexP1 = re.compile("^[0-9]*$")

        findeP1 = regexP1.match(firsttow)

        if firsttow != "09":
            raise HTTPException(detail="شماره وارد شده مطابق استاندارد شماره های کشور جمهوری اسلامی ایران نمی باشد",
                                status_code=status.HTTP_400_BAD_REQUEST)
        if len1 >= 12 or len1 <= 10:
            raise HTTPException(detail="ارقام وارده باید 11 رقم باشد", status_code=status.HTTP_400_BAD_REQUEST)
        if not findeP1:
            raise HTTPException(detail="شماره وارد شده نادرست است لطفا فقط از اعداد استفاده کنید",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "شماره وارد شده صحیح است"
    @validator("SHphone")
    def SHP(SHphone):
        phoneH = str(SHphone)
        len1 = int(len(str(phoneH)))
        code = str(phoneH)[:3]
        first = str(phoneH)[3:4]
        allcode = ["086", "021", '025', '041', '044', '045', '031', '026', '084', '077',
                   '028', '071', '054', '023', '024', '058', '061', '051', '056', '038',
                   '087', '034', '083', '013', '017', '074', '066', '011', '076', '081', '035']
        allfirst = ['3', '4', '5', '8']

        regexH = re.compile("^[0-9]*$")

        findeH = regexH.match(phoneH)

        if code not in allcode:
            raise HTTPException(detail="کد شهرستان وارد شده نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if first not in allfirst:
            raise HTTPException(detail="رقم اول بعد از کد شهرستان نادرست است", status_code=status.HTTP_400_BAD_REQUEST)
        if len1 >= 12 or len1 <= 10:
            raise HTTPException(detail="ارقام وارده باید 11 رقم باشد", status_code=status.HTTP_400_BAD_REQUEST)
        if not findeH:
            raise HTTPException(detail="شماره وارد شده نادرست است لطفا فقط از اعداد استفاده کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "شماره وارد شده صحیح است"
    @validator("Sdepartment")
    def SD(Sdepartment: str):
        allDepartment = ["فنی و مهندسی", "علوم پایه",
                         "شیمی", "اقتصاد", 'ادبیات', "دامپزشکی"]

        if Sdepartment not in allDepartment:
            raise HTTPException(detail="دانشکده وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "دانشکده وارد شده، ثبت شد."
    @validator("Smajor")
    def SMajor(Smajor: str):
        allmajor = ["برق", "کامپیوتر",
                    "عمران", "معماری", 'مکانیک', "دامپزشکی", "حقوق", "روانشناسی", "مدیریت بازرگانی", "صنایع",
                    "تربیت بدنی"]

        if Smajor not in allmajor:
            raise HTTPException(detail="رشته وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "رشته وارد شده صحیح است"
    @validator("Smarried")
    def SMarried(Smarried: str):
        maritalstatus = ["متاهل", "مجرد"]

        if Smarried not in maritalstatus:
            raise HTTPException(detail="لطفا یکی از دو گزینه مجرد و یا متاهل را وارد کنید",
                                status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "وضعیت وارد شد"
    @validator("SNid")
    def SNC(SNid):
        code = str(SNid)
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

    @validator("course_numbers")
    def TCN(cls, courses):
        try:
            courses = courses.split(",")
            for course in courses:
                a = int(course)
        except:
            raise ValueError("Courses id must separate by ,")

        for course in courses:
            course =  crud.get_Course(db, int(course))
            if course is None:
                raise ValueError("Courses id is not correct!")

        return "کد دروس وارد شده ثبت شد."

    @validator("SLid")
    def STID(cls, value):
        try:
            teachers = value.split(",")
            for teacher in teachers:
                a = int(teacher)
        except:
            raise ValueError("Teacher id must separate by ,")

        for teacher in teachers:
            teacher =  crud.get_Teacher(db, int(teacher))
            if teacher is None:
                raise ValueError("Teacher id is not correct!")

        return "کد اساتید وارد شده ثبت شد."
