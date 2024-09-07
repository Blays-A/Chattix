from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    bio = models.CharField(max_length=350)
    phone = models.IntegerField(null=True , blank=True)
    image = models.ImageField(upload_to='profile_pic' ,  max_length=500 , blank=True , null=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"
    
    # def get_absolute_url(self):
    #     return reverse('social_media:profile',
    #                     args=[self.id, self.slug])