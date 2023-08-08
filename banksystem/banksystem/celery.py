import os
from celery.schedules import crontab

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banksystem.settings')

app = Celery('banksystem')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'execute-task-after-login': {
        'task': 'users.tasks.add',
        'schedule': crontab(minute='*/15'),
        'args': (12345678, 12345678),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
