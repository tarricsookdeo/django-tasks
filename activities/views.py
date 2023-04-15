from django.shortcuts import render

from .models import Activity


def index(request):
    activity = Activity.objects.first()
    context = {'activity': activity}
    return render(request, 'activities/activity.html', context)
