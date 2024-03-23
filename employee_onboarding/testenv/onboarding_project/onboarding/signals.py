from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User

@receiver(user_logged_in, sender=User)
def send_login_notification(sender, user, request, **kwargs):
    subject = 'Login Notification'
    message = f'Hello {user.username},\n\nYou have successfully logged into your account.'
    from_email = 'your@email.com'  # Enter your email address
    to_email = user.email
    send_mail(subject, message, from_email, [to_email])
