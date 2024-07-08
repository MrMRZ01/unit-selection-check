
import re


# def StudentCity(City):
#     city = City
#
#     regex = re.compile("^[آ-ی]*$")
#
#     findere = regex.match(city)
#
#     # if city == int:
#     if not findere:
#         print( "لطفا نام شهر را به فارسی وارد کنید و از اعداد استفاده نکنید")
#     else:
#         print("شهر وارد شده درست است")
#
#
# City = input("enter your city:")
# StudentCity(City)

# ---------------------------------------------------------------------------------------------------
# def S(Serial):
#
#     alpha = (str(Serial)[:1])
#     townum = int(str(Serial)[2:4])
#     sixnum = int(str(Serial)[4:10])
#     len1 = int(len(str(Serial)))
#     # allalpha = ["آ", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د",
#     #             "ذ", "ر", "ز", "ط", "ظ", "ع", "غ", "ک", "گ", "ل", "ض",
#     #             "ص", "ف", "ق", "ن", "ی", "س", "ش", "ژ", "و", "م"]
#     allalpha = alpha
#
#     regexS = re.compile("^[آ-ی]$")
#
#     findeS = regexS.match(allalpha)
#
#     if len1 >= 10 or len1 <= 8:
#         print( "تعداد کاراکتر های وارد شده نادرست است")
#     if not findeS:
#         print ("حرف فارسی وارد شده نادرست است")
#     if not isinstance(townum, int):
#         print ("بخش دو رقمی حتما باید عدد باشد")
#     if not isinstance(sixnum, int):
#         print ("بخش شش رقمی نیز حتما باید عدد باشد")
#
#     else:
#         print ("شماره شناسنامه وارد شده صحیح است")
#
# Serial= input("enter serial number")
# S(Serial)

# ---------------------------------------------------------------------------------
import re
# def S(Postal):
#     postal = Postal
#     len1 = len(postal)
#
#     regexP = re.compile("^[0-9]*$")
#
#     findeP = regexP.match(postal)
#
#
#     if len1 >= 11 or len1 <= 9:
#         print ("تعداد ارقام وارد شده نادرست است. کد پستی باید 10 رقم باشد")
#
#     if not findeP:
#         print("کدپستی وارد شده نادرست است، لطفا فقط از اعداد استفاده کنید.")
#
#     print ("کدپستی وارد شده صحیح است")
#
# Postal = input("enter postal code: ")
#
# S(Postal)

# -----------------------------------------------------------------------------------------------
#
# def S(Phone):
#     phone = Phone
#     firsttow = str(phone[:2])
#     len1 = int(len(str(phone)))
#
#     regexP1 = re.compile("^[0-9]*$")
#
#     findeP1 = regexP1.match(phone)
#
#     if firsttow != "09":
#         print ("شماره وارد شده مطابق استاندارد شماره های کشور جمهوری اسلامی ایران نمی باشد")
#     if len1 >= 12 or len1 <= 10:
#         print( "ارقام وارده باید 11 رقم باشد")
#
#     if not findeP1:
#         print("شماره وارد شده نادرست است لطفا، فقط ازاعداد استفاده کنید.")
#
#     print( "شماره وارد شده صحیح است")
#
# Phone = input ("enter your number phone:")
#
# S(Phone)
#

# -----------------------------------------------------------------------------------------------------------
#
# def StudentPone(StudentPhoneHome):
#     phoneH = StudentPhoneHome
#     len1 = int(len(str(phoneH)))
#     code = str(phoneH)[:3]
#     first = str(phoneH)[3:4]
#     allcode = ["086","021",'025','041','044','045','031','026','084','077',
#                '028','071','054','023','024','058','061','051','056','038',
#                '087','034','083','013','017','074','066','011','076','081','035']
#     allfirst = ['3','4','5','8']
#
#     if code not in allcode:
#         return "کد شهرستان وارد شده نادرست است"
#     if first not in allfirst:
#         return "رقم اول بعد از کد شهرستان نادرست است"
#     if len1 >= 12 or len1 <= 10:
#         return "ارقام وارده باید 11 رقم باشد"
# -----------------------------------------------------------------------------------------------------------

import re

n = int(input())
n = f"{n}"
regex = re.compile("^[1-4]$")

finde = regex.match(n)

if not finde:
    print("لطفا از اعداد 1 تا 4 برای تعداد واحد استفاده کنید")
    exit()

lenn = len(n)
print(lenn)