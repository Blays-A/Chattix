from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=200 , db_index=True)
    caption = models.CharField(max_length=1500)
    img = models.ImageField(upload_to='product/video/%Y' , blank=True ,  max_length=500 , null=True)
    video = models.FileField()
    slug = models.SlugField(max_length=200, db_index=True , unique= True )
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='videos')


    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('social_media:video_detail',
                        args=[self.id, self.slug])
    
    


class Comment(models.Model):
    video = models.ForeignKey(Video , on_delete= models.CASCADE , related_name='comment')
    text = models.TextField(max_length=1500 , null=True , blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.text} by {self.author}'