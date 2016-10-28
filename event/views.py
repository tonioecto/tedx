from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    speakers= Speaker.objects.all()
    return(render(request, "event/index.html",{'speakers':speakers}))

def speaker(request):
    speakers= Speaker.objects.all()
    prevSpeakers=PreviousSpeaker.objects.all()
    years=PreviousSpeaker.objects.values('year').distinct()
    return render(request, "event/speaker.html",{'speakers':speakers,'prevSpeakers':prevSpeakers,'years':years})
