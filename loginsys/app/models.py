from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    username = models.OneToOneField(User,on_delete = models.CASCADE)
    contact = models.IntegerField()
    email = models.EmailField()
    profile_Picture = models.ImageField(upload_to='imgs')
    def __str__(self):
        return str(self.username)
