import re
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sql_app import models


class DataValidation:

    def cid_exists(db: Session, cid: str):
        course_exists = db.query(models.Course).filter(models.Course.cid == cid).first()
        if not course_exists:
            raise HTTPException(status_code=404, detail="Course not found")


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

    def CN(CName):

        regexN100 = re.compile("^[آ-ی 1-4]*$")

        findeN100 = regexN100.match(CName)

        if len(CName) > 20:
            raise HTTPException(detail="حروف نام درس نباید بیش از 20 کاراکتر باشد.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        if len(CName) < 3:
            raise HTTPException(detail="نام درس باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

        if not findeN100:
            raise HTTPException(detail="نام درس وارد شده نامعتبر است، لطفا نام را به حروف فارسی وارد کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return ("نام درس ثبت شد.")

    def CD(CDepartment: str):
        allDepartment1 = ["فنی و مهندسی", "علوم پایه",
                          "شیمی", "اقتصاد", 'ادبیات', "دامپزشکی"]

        if CDepartment not in allDepartment1:
            raise HTTPException(detail="دانشکده وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "دانشکده وارد شده ثبت شد."

    def CR(Credit):

        regexcr = re.compile("^[1-4]$")
        findcr = regexcr.match(Credit)

        if not findcr:
            raise HTTPException(detail="لطفا برای واحد درس فقط از اعداد یک تا چهار استفاده نمایید.",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "واحد درس ثبت شد."

# ------------------------------------------------------------------------------------------
# استاد:

    def Tid_exists(db: Session, Tid: str):
        Teacher_exists = db.query(models.Teacher).filter(models.Teacher.Tid == Tid).first()
        if not Teacher_exists:
            raise HTTPException(status_code=404, detail="Teacher not found")


    def TN(TName):

        regexN10 = re.compile("^[آ-ی ]*$")

        findeN10 = regexN10.match(TName)

        if len(TName) > 10:
            raise HTTPException(detail="حروف نام نباید بیش از 10 کاراکتر باشد.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        if len(TName) < 3:
            raise HTTPException(detail="نام باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

        if not findeN10:
            raise HTTPException(detail="نام وارد شده نامعتبر است، لطفا نام را به حروف فارسی وارد کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return ("نام ثبت شد.")

    def TF(TFamily):

        regexN20 = re.compile("^[آ-ی ]*$")

        findeN20 = regexN20.match(TFamily)

        if len(TFamily) > 15:
            raise HTTPException(detail="حروف فامیلی نباید بیش از 15 کاراکتر باشد.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        if len(TFamily) < 3:
            raise HTTPException(detail="فامیلی باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

        if not findeN20:
            raise HTTPException(detail="فاملی وارد شده نامعتبر است، لطفا فامیلی را به حروف فارسی وارد کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return ("فامیلی ثبت شد.")

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

    def TD(TDepartment: str):
        allDepartment1 = ["فنی و مهندسی", "علوم پایه",
                          "شیمی", "اقتصاد", 'ادبیات', "دامپزشکی"]

        if TDepartment not in allDepartment1:
            raise HTTPException(detail="دانشکده وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "دانشکده وارد شده ثبت شد."

    def TM(TMajor: str):
        allmajor1 = ["برق", "کامپیوتر",
                     "عمران", "معماری", 'مکانیک', "دامپزشکی", "حقوق", "روانشناسی", "مدیریت بازرگانی", "صنایع",
                     "تربیت بدنی"]

        if TMajor not in allmajor1:
            raise HTTPException(detail="رشته وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "رشته وارد شده صحیح است"

    def TB(TBirth):
        year1 = int(str(TBirth)[:4])
        month1 = int(str(TBirth)[4:6])
        day1 = int(str(TBirth)[6:8])
        len10 = int(len(str(TBirth)))

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

    def TA(TAddress):
        address = TAddress
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

    def TP(TPostal):
        postal1 = TPostal
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

    def TPH(TPhone):
        phone1 = TPhone
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

    def THP(THPhone):
        phoneH1 = THPhone
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

    def TCI(TCID):

        len31 = len(TCID)

        regextcid = re.compile("^[0-9]*$")
        findtcid = regextcid.match(TCID)

        if len31 != 5:
            raise HTTPException(detail="شماره درس باید 5 رقم باشد.", status_code=status.HTTP_400_BAD_REQUEST)
        if not findtcid:
            raise HTTPException(detail="لطفا برای شماره درس فقط از اعداد استفاده نمایید.",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "شماره درس ثبت شد."

    def TI(TID):

        len30 = len(TID)

        regextid = re.compile("^[0-9]*$")
        findtid = regextid.match(TID)

        if len30 != 6:
            raise HTTPException(detail="شماره استادی باید 6 رقم باشد.", status_code=status.HTTP_400_BAD_REQUEST)
        if not findtid:
            raise HTTPException(detail="لطفا برای شماره استادی فقط از اعداد استفاده نمایید.",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "شماره استادی ثبت شد."

# -------------------------------------------------------------------------------------

# دانشجو:

    def Sid_exists(db: Session, Sid: str):
        Student_exists = db.query(models.Student).filter(models.Student.Sid == Sid).first()
        if not Student_exists:
            raise HTTPException(status_code=404, detail="Student not found")
    def StudentNumber(StudentNumber):
        year = int(str(StudentNumber)[:3])
        constant_part = str(StudentNumber)[3:9]
        index = int(str(StudentNumber)[9:])
        len1 = int(len(str(StudentNumber)))

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

    def StudentFamily(StudentFamily):

        regexN2 = re.compile("^[آ-ی ]*$")

        findeN2 = regexN2.match(StudentFamily)

        if len(StudentFamily) > 15:
            raise HTTPException(detail="حروف فامیلی نباید بیش از 15 کاراکتر باشد.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        if len(StudentFamily) < 3:
            raise HTTPException(detail="فامیلی باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

        if not findeN2:
            raise HTTPException(detail="فاملی وارد شده نامعتبر است، لطفا فامیلی را به حروف فارسی وارد کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return ("فامیلی ثبت شد.")

    def StudentName(StudentName):

        regexN1 = re.compile("^[آ-ی ]*$")

        findeN1 = regexN1.match(StudentName)

        if len(StudentName) > 10:
            raise HTTPException(detail="حروف نام نباید بیش از 10 کاراکتر باشد.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        if len(StudentName) < 3:
            raise HTTPException(detail="نام باید حداقل 3 حرف داشته باشد.", status_code=status.HTTP_400_BAD_REQUEST)

        if not findeN1:
            raise HTTPException(detail="نام وارد شده نامعتبر است، لطفا نام را به حروف فارسی وارد کنید.",
                                status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return ("نام ثبت شد.")

    def StudentBirth(StudentBirth):
        year = int(str(StudentBirth)[:4])
        month = int(str(StudentBirth)[4:6])
        day = int(str(StudentBirth)[6:8])
        len1 = int(len(str(StudentBirth)))

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

    def StudentState(StudentState):
        state = str(StudentState)
        allstate = ["قم", "مرکزی", "تهران", "لرستان",
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

    def StudentCity(StudentCity):
        city = StudentCity

        regex = re.compile("^[آ-ی]*$")

        findere = regex.match(city)

        # if city == int:
        if not findere:
            raise HTTPException(detail="لطفا نام شهر را به فارسی وارد کنید و از اعداد استفاده نکنید",
                                status_code=status.HTTP_400_BAD_REQUEST)
        else:
            return "شهر وارد شده درست است"

    def StudentAddress(StudentAddress):
        address = StudentAddress
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

    def StudentPostal(StudentPostal):
        postal = StudentPostal
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

    def StudentPone(StudentPhone):
        phone = StudentPhone
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

    def StudentPone(StudentPhoneHome):
        phoneH = StudentPhoneHome
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

    def StudentDepartment(StudentDepartment: str):
        allDepartment = ["فنی و مهندسی", "علوم پایه",
                         "شیمی", "اقتصاد", 'ادبیات', "دامپزشکی"]

        if StudentDepartment not in allDepartment:
            raise HTTPException(detail="دانشکده وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "دانشکده وارد شده، ثبت شد."

    def StudentMajor(StudentMajor: str):
        allmajor = ["برق", "کامپیوتر",
                    "عمران", "معماری", 'مکانیک', "دامپزشکی", "حقوق", "روانشناسی", "مدیریت بازرگانی", "صنایع",
                    "تربیت بدنی"]

        if StudentMajor not in allmajor:
            raise HTTPException(detail="رشته وارد شده نادرست است", status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "رشته وارد شده صحیح است"

    def StudentMarital(StudentMarital: str):
        maritalstatus = ["متاهل", "مجرد"]

        if StudentMarital not in maritalstatus:
            raise HTTPException(detail="لطفا یکی از دو گزینه مجرد و یا متاهل را وارد کنید",
                                status_code=status.HTTP_404_NOT_FOUND)
        else:
            return "وضعیت وارد شد"

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

