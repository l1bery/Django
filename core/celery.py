import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django apps.
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send-email-message': {
        'task': 'apps.users.tasks.send_email_task',
        'schedule': 10.0, #Это каждую секунду ,
        # 'schedule': crontab(hour=19, minute=58),
        'kwargs': {}
    }


}