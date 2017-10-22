from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chocfruitbox.settings')

app = Celery('chocfruitbox')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_recs_email': {
        'task': 'choc_customer.tasks.send_recs',
        'schedule': crontab(hour=6, minute=0),
        'args': (),
    },
    'charge_order': {
        'task': 'order.tasks.process_order',
        'schedule': crontab(hour=23, minute=0),
        'args': (),
    }
}