from django.db import models
from content.models import *
from reg_school.models import *
from django.contrib.auth.models import User


class TeacherClass(models.Model):
    id = models.AutoField(primary_key = True , unique = True)
    teacher = models.ForeignKey(User , on_delete = models.CASCADE)
    clas = models.ForeignKey(Classes , on_delete = models.CASCADE)
    limit = models.CharField(max_length=2)
    school = models.ForeignKey(School , on_delete = models.CASCADE , null=True,blank = True)
    def __str__(self):
        return 'Class {} Of {}'.format(self.clas,self.teacher)

class TeacherClassStudents(models.Model):
    id = models.AutoField(primary_key = True , unique = True)
    clas = models.ForeignKey(TeacherClass , on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=11)
    address = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='static/class/pictures/' , blank=True , null=True)
    def __str__(self):
        return 'Student {} Of {}'.format(self.name,self.clas)