from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=10000)
    phone = models.IntegerField(blank=True,null=True)
    image = models.ImageField(default='default.jpg', upload_to="profile_pic")


    def __str__(self):
        return f'{self.user.username} - Profile'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            out_size = (300,300)
            img.thumbnail(out_size)
            img.save(self.image.path)








































