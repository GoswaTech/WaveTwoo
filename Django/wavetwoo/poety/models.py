from django.db import models
from datetime import datetime


# Create your models here.
class SnapPoety(models.Model):

    title = models.CharField(max_length=63)
    image = models.ImageField(upload_to='images/snappoety')
    text = models.TextField(max_length=2047)
    date = models.DateTimeField(auto_now_add=True)
    history = models.ForeignKey('SnapHistory', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0} : {1} ({2})'.format(self.title, self.text, self.date)

class SnapHistory(models.Model):

    slug = models.SlugField(max_length=63, unique=True)
    name = models.CharField(max_length=63)
    description = models.TextField(max_length=1023)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} : {1} ({2})'.format(self.name, self.description, self.date)
