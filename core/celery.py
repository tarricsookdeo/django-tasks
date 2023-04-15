import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')

app.conf.enable_utc = False

app.conf.update(timezone='America/New_York')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update-activity-every-30-seconds': {
        'task': 'activities.tasks.update_activity',
        'schedule': timedelta(seconds=30)
    }
}

# COMMANDS TO RUN
# celery -A core worker -l info - this starts the celery worker
# celery -A core beat -l info -  this starts the celery beat worker
