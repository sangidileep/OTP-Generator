import random
import smtplib
from twilio.rest import Client
otp = random.choice(range(100000, 1000000))

def otp_generation_mail():
    s_mail = "sangidileepchakravarthi@gmail.com"
    password = "bfcsavaljidtpezz"
    r_mail=input("Enter Mail id to send otp")
    message=f'OTP to login-{otp}'

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(s_mail,password)
    print('login successful')
    server.sendmail(s_mail,r_mail,message)
    print('OTP send')

def otp_generation_sms():
    phone=input("Enter phone no to send otp")
    account_sid = "ACb1df7bdb6882ffe12ae484a53ed4dd35"
    auth_token = "a1c835fe2ab230044dd467b9abce05f4"
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body=f'OTP to login-{otp}',
        from_='+13526453534',
        to=phone
    )

def otp_verification():
    otp_generation=otp
    otp_ver=int(input('Enter OTP '))
    if otp_ver == otp_generation:
        print('OTP Verified Successfully')
    else:
        print('OTP is Invalid reenter again')
        otp_verification()
if __name__== "__main__":
    while True:
        print('1. To verify otp by mail')
        print('2. To verify otp by mobile no')
        val = int(input(""))
        if val == 1:
            otp_generation_mail()
            otp_verification()
        elif val == 2:
            otp_generation_sms()
            otp_verification()
        exit()