from django.db import models
from requirments.models import *
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Module(models.Model):
    code = models.AutoField(primary_key = True)
    module = models.CharField(max_length=250)
    def __str__(self):
        return self.module

class Content(models.Model):
    code = models.AutoField(primary_key = True)
    class_name = models.ForeignKey(Classes , on_delete = models.CASCADE)
    subject = models.ForeignKey(Subjects , on_delete = models.CASCADE)
    module = models.ForeignKey(Module , on_delete = models.CASCADE)
    date = models.DateField()
    day = models.IntegerField()
    title = models.CharField(max_length=250)
    text = models.TextField(null = True)
    therefor = models.CharField(max_length = 20 ,choices=(('S','Self-Paced'),('O','Online-School')))
    def __str__(self):
        return self.title

class Videos(models.Model):
    content = models.ForeignKey(Content , on_delete = models.CASCADE)
    url = models.URLField(max_length=500)

class Images(models.Model):
    content = models.ForeignKey(Content , on_delete = models.CASCADE)
    image = models.ImageField(upload_to='static/products/', storage=gd_storage)
