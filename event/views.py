
from django.shortcuts import get_object_or_404, render
from .models import *
# Create your views he#re.
def index(request):
    speakers= Speaker.objects.all()
    return(render(request, "event/index.html",{'speakers':speakers}))

def speaker(request):
    speakers= Speaker.objects.all()
    prevSpeakers=PreviousSpeaker.objects.all()
    years=PreviousSpeaker.objects.values('year').distinct()
    return render(request, "event/speaker.html",{'speakers':speakers,'prevSpeakers':prevSpeakers,'years':years})

def speaker_list():
    return Speaker.objects.all()

def speakerPage(request, name):
    speaker=get_object_or_404(Speaker, name=name)
    return render(request,'event/speakerPage.html',{'speaker':speaker})
