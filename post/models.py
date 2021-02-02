from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=50)
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
    image=models.ImageField(blank=True,upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view',kwargs={'id':self.id})
