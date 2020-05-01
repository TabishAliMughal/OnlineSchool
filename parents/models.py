from django.db import models
from django.contrib.auth.models import User
from teacher.models import *

class StudentPairent(models.Model):
    code = models.AutoField(primary_key = True)
    parent = models.ForeignKey(User, on_delete = models.CASCADE)
    student = models.ForeignKey(TeacherClassStudents ,on_delete=models.CASCADE)
