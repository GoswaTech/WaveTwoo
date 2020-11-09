from django.db import models
from datetime import datetime


# Create your models here.
class SnapPoety(models.Model):

    title = models.CharField(max_length=63)
    image = models.ImageField(upload_to='images/snappoety')
    text = models.TextField(max_length=2047)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} : {1} ({2})'.format(self.title, self.text, self.date)
