
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import Participant
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
# Create your views he#re.
def index(request):
    speakers= Speaker.objects.all()
    return(render(request, "event/index.html",{'speakers':speakers}))

def speaker(request):
    speakers= Speaker.objects.all()
    prevSpeakers=PreviousSpeaker.objects.all()
    years=PreviousSpeaker.objects.values('year').distinct()
    return render(request, "event/speaker.html",{'speakers':speakers,'prevSpeakers':prevSpeakers,'years':years})

def particip(request):
    speakers= Speaker.objects.all()
    if request.method=='POST':
        form= Participant(request.POST)
        if form.is_valid():
            if (form.cleaned_data["value"]=="1"):
                p=Participants(name=form.cleaned_data["name"],email=form.cleaned_data["email"])
                p.save()
                return (render(request, "event/index.html",{'speakers':speakers}))
            else:
                return HttpResponseRedirect("https://www.google.com")


def speakerPage(request, id):
    speaker=get_object_or_404(Speaker, id=id)
    return render(request,'event/speakerPage.html',{'speaker':speaker})

def prevSpeakerPage(request, id):
    speaker=get_object_or_404(PreviousSpeaker, id=id)
    return render(request,'event/speakerPage.html',{'speaker':speaker})
