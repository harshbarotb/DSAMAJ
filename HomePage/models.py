from django.db import models


# Create your models here.

class NewsAndEventsBlog(models.Model):
    Id = models.AutoField
    BlogId = models.CharField(null=False, max_length=200)
    NewsTitle = models.CharField(null=False, max_length=500)
    NewsDate = models.DateField(null=False)
    NewsThumbnailTitleNews = models.CharField(null=False, max_length=200)
    NewsImages = models.ImageField(upload_to='newsImages')
    NewsBlogNews = models.CharField(null=False, max_length=10000)
    Created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
