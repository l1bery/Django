from celery import shared_task
from django.core.mail import send_mail

from core import settings

@shared_task
def send_email_task():
    subject = 'Welcome'
    message = 'ПОПЛАЧЬ'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['nursulpen@gmail.com']
    send_mail(subject, message, email_from, recipient_list, fail_silently=False,)
