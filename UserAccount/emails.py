from django.core.mail import send_mail
import random
from django.conf import settings
from .models import Employee_Profile
def send_otp_via_email(email):
    subject = 'Your Account Verification Email'
    otp = random.randint(100000, 999999)
    message =f'Your OTP for login is {otp} '
    email_from = settings.EMAIL_HOST
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)
    user_obj = Employee_Profile.objects.get(employee_email=email)
    user_obj.otp = otp
    user_obj.save()