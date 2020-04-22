from django.db import models
from requirments.models import *
from teacher.models import *


class Semester(models.Model):
    code = models.AutoField(primary_key = True)
    semester = models.CharField(max_length=200 , unique = True)
    def __str__(self):
        return self.semester
    
class Session(models.Model):
    code = models.AutoField(primary_key = True)
    session = models.CharField(max_length=200 , unique = True)
    def __str__(self):
        return self.session
    
    
class ExamStatus(models.Model):
    code = models.AutoField(primary_key = True)
    class_name = models.ForeignKey(Classes, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subjects ,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester ,on_delete=models.CASCADE)
    session = models.ForeignKey(Session ,on_delete=models.CASCADE)
    status = models.BooleanField()
    def __str__(self):
        return 'Exam of {} Class {} and Session {} {} Semister'.format(self.subject,self.class_name,self.session,self.semester)

class ExamQuestions(models.Model):
    code = models.AutoField(primary_key = True)
    exam = models.ForeignKey(ExamStatus , on_delete = models.CASCADE)
    file = models.FileField(upload_to='static/exam/papers/', blank = True)
    question = models.CharField(max_length = 250, blank = True)
    marks = models.IntegerField(blank = True)
    def __str__(self):
        return 'Question Of Class {} Session {} {} Semester'.format(self.exam.class_name,self.exam.session,self.exam.semester)

class ExamAnswers(models.Model):
    code = models.AutoField(primary_key=True)
    student = models.ForeignKey(TeacherClassStudents , on_delete=models.CASCADE)
    exam = models.ForeignKey(ExamStatus , on_delete = models.CASCADE)
    picture = models.ImageField(upload_to='static/exam/papers/answers/')
    checked = models.BooleanField()

