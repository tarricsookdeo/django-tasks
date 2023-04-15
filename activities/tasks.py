import requests
from celery import shared_task
from celery.utils.log import get_task_logger

from .models import Activity

logger = get_task_logger(__name__)


@shared_task
def update_activity():
    activity = Activity.objects.first()
    response = requests.get('http://www.boredapi.com/api/activity/')
    data = response.json()
    activity.activity = data['activity']
    activity.type = data['type']
    activity.participants = data['participants']
    activity.price = data['price']
    activity.link = data['link']
    activity.save()
    logger.info('Activity updated')
