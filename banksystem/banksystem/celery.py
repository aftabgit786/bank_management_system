import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banksystem.settings')

app = Celery('banksystem')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'execute-task-after-login': {
        'task': 'users.tasks.add',
        'schedule': timedelta(seconds=10),
        'args': (12345678, 12345678),
    },
}

app.conf.beat_schedule_filename = "banksystem/celerybeat-schedule"


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
