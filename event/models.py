from django.db import models

# Create your models here.
class Speaker(models.Model):
    name = models.CharField("Nom du speaker", max_length=254)
    description = models.TextField("Description", blank=True)
    image = models.FileField("Image :", upload_to='media/speakers')
    def __str__(self):              # __unicode__ on Python 2
        return self.name
