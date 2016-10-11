from django.shortcuts import render
from models import *
# Create your views here.
def index(request):
    return(render(request, "event/index.html"))

def speaker(request):
    speakers= Speaker.objects.all()
    return render(request, "event/speaker.html",{'speakers':speakers})
