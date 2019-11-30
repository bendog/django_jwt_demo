from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

FROM_EMAIL = "django@fitzhardinge.net"
SITE_DOMAIN = "127.0.0.1:8000"
SITE_NAME = ""
USE_HTTPS = False


def send_password_reset_email(user):
    PasswordResetForm().send_mail(
        subject_template_name="registration/password_reset_subject.txt",
        email_template_name="registration/password_reset_email.html",
        context={
            "email": user.email,
            "domain": SITE_DOMAIN,
            "site_name": SITE_NAME,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "user": user,
            "token": PasswordResetTokenGenerator().make_token(user),
            "protocol": "https" if USE_HTTPS else "http",
        },
        from_email=FROM_EMAIL,
        to_email=user.email,
    )
    return
