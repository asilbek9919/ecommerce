from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

TYPE_CHOICE = (
    ('All','All'),
    ('Kids','Kids')
)

MOVIE_TYPE = (
    ('Single','Single'),
    ('Serial','Serial')
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profiles')

class Profiles(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=5,choices= TYPE_CHOICE)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    
    def __str__(self):
        return self.name + " " + self.age_limit


class Movie(models.Model):
    title = models.CharField(max_length=225)
    descriptions = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4,unique=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    videos = models.ManyToManyField('Video')
    flay = models.ImageField(upload_to='fleyrs',blank=True,null=True)
    age_limit = models.CharField(max_length=5,choices=TYPE_CHOICE,blank=True,null=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    file = models.FileField(upload_to='movies')


    def __str__(self):
        return self.title


















