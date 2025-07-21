from celery import shared_task
from django.core.mail import send_mail
import requests

from core import settings

@shared_task
def send_email_task():
    subject = 'Welcome'
    message = 'ПОПЛАЧЬ'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['nursulpen@gmail.com']
    send_mail(subject, message, email_from, recipient_list, fail_silently=False,)

@shared_task
def     send_tg_message(chat_id ,text):
    token = settings.TG_BOT_TOKEN
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text,
    }
    response = requests.post(url, data=data)
    return response.json()