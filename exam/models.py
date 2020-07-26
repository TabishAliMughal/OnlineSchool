from django.db import models
from requirments.models import *
from teacher.models import *
from indivisuals.models import *


# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

class ExamStatus(models.Model):
    code = models.AutoField(primary_key = True)
    exam_number = models.IntegerField()
    class_name = models.ForeignKey(Classes, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subjects ,on_delete=models.CASCADE)
    session = models.ForeignKey(Session ,on_delete=models.CASCADE)
    status = models.BooleanField()
    def __str__(self):
        return 'Exam of {} Class {} and Session {}'.format(self.subject,self.class_name,self.session)

class ExamQuestions(models.Model):
    code = models.AutoField(primary_key = True)
    exam = models.ForeignKey(ExamStatus , on_delete = models.CASCADE)
    file = models.ImageField(upload_to='static/exam/papers/', blank = True , storage=gd_storage)
    question = models.CharField(max_length = 250, blank = True)
    marks = models.IntegerField(blank = True)
    def __str__(self):
        return 'Question Of Class {} Session {}'.format(self.exam.class_name,self.exam.session)

class ExamAnswers(models.Model):
    code = models.AutoField(primary_key=True)
    student = models.ForeignKey(Indivisuals , on_delete=models.CASCADE)
    exam = models.ForeignKey(ExamStatus , on_delete = models.CASCADE)
    picture = models.ImageField(upload_to='static/exam/papers/answers/' , storage=gd_storage)
    checker = models.ForeignKey(User , on_delete=models.CASCADE,blank=True,null=True)
    checked = models.CharField(max_length=8)
    def __str__(self):
        return 'Answer Of {}'.format(self.student)

class QuestionsChecked(models.Model):
    code = models.AutoField(primary_key=True)
    checker = models.ForeignKey(User , on_delete = models.CASCADE)
    question = models.ForeignKey(ExamQuestions , on_delete=models.CASCADE)
    student = models.ForeignKey(Indivisuals , on_delete=models.CASCADE)
    obtained = models.IntegerField()
    def __str__(self):
        return 'Answer Of {} , Checked By {}'.format(self.student,self.checker)

class Guide(models.Model):
    code = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subjects ,on_delete=models.CASCADE)
    url = models.URLField(max_length=500)
