from django.db import models
from django.utils import timezone


class Pict(models.Model):
    comment = models.TextField(max_length=300)
    date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(null=True, upload_to="gallery")


    image_height = 800
    image_width = 600
    

    

