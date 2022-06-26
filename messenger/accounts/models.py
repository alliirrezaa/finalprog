from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Phone=models.IntegerField(null=True,blank=True)
    profile_image=models.ImageField(upload_to="%y/%m/%d",default="d.jpeg",null=True,blank=True)
    
    def __str__(self):
        return self.user.username

def save_profile(sender,**kwargs):
    if kwargs['created']:
        profile_user=Profile(user=kwargs['instance'])
        profile_user.save()

post_save.connect(save_profile,sender=User)