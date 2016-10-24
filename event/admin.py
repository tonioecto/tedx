from django.contrib import admin
from .models import Speaker, PreviousSpeaker
# Register your models here.
admin.site.register(Speaker)
admin.site.register(PreviousSpeaker)
