import requests
from celery import shared_task
from celery.utils.log import get_task_logger

from .models import Activity

logger = get_task_logger(__name__)


@shared_task
def update_activity():
    # Get the first activity, we only have one
    activity = Activity.objects.first()

    # Get the activity from the Bored API
    response = requests.get('http://www.boredapi.com/api/activity/')
    data = response.json()

    # Update the activity
    activity.activity = data['activity']
    activity.type = data['type']
    activity.participants = data['participants']
    activity.price = data['price']
    activity.link = data['link']

    # Save the activity
    activity.save()

    # Log that the activity was updated
    logger.info('Activity updated')
