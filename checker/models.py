from django.db import models
from django.contrib.auth.models import User
from requirments.models import *
from teacher.models import *
from exam.models import *


class CheckerClass(models.Model):
    id = models.AutoField(primary_key = True , unique = True)
    checker = models.ForeignKey(User , on_delete = models.CASCADE)
    subject = models.ForeignKey(ClassSubjects , on_delete = models.CASCADE)
    def __str__(self):
        return 'Checker {} of {}'.format(self.checker,self.subject)

class CheckedCount(models.Model):
    id = models.AutoField(primary_key = True , unique = True)
    checker = models.ForeignKey(User , on_delete = models.CASCADE)
    student = models.ForeignKey(TeacherClassStudents , on_delete = models.CASCADE)
    exam = models.ForeignKey(ExamStatus,on_delete = models.CASCADE)
    count = models.IntegerField()
    def __str__(self):
        return 'Checking of {} of {}'.format(self.checker,self.exam)
