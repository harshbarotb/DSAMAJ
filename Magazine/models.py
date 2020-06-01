from django.db import models


# Create your models here.


class MagazineUpload(models.Model):
    id = models.AutoField
    Magazine_Cover_Page = models.ImageField(upload_to='magazine/thumbnilimages')
    Magazine_Cover_Title = models.CharField(null=False, max_length=500)
    Magazine_Link = models.CharField(null=True, max_length=500)
    Date = models.DateField(auto_now_add=True)
    objects = models.Manager()


class EventCode(models.Model):
    id = models.AutoField
    Event_Id = models.CharField(null=True, max_length=200)
    Date = models.DateField(auto_now_add=True)
    objects = models.Manager()


class EventSection(models.Model):
    id = models.AutoField
    Event_Id = models.ForeignKey(EventCode, on_delete=models.CASCADE)
    Re_Enter_Id = models.CharField(null=True, max_length=500)
    Event_Cover_Page = models.ImageField(upload_to='EventCoverImages')
    Event_Cover_Title = models.CharField(null=False, max_length=500)
    Date = models.DateField(auto_now_add=True)
    objects = models.Manager()


class EventImages(models.Model):
    id = models.AutoField
    Event_Id = models.ForeignKey(EventCode, on_delete=models.CASCADE)
    Re_Enter_Id = models.CharField(null=True, max_length=500)
    Upload_Image = models.ImageField(upload_to='PhotoS')
    Date = models.DateField(auto_now_add=True)
    objects = models.Manager()
