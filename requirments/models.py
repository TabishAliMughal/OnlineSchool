from django.db import models



class Classes(models.Model):
    code = models.AutoField(primary_key = True)
    class_name = models.CharField(max_length=200 , unique = True)
    def __str__(self):
        return self.class_name

class Subjects(models.Model):
    code = models.AutoField(primary_key = True)
    subject_name = models.CharField(max_length=200 , unique = True)
    def __str__(self):
        return self.subject_name

class ClassSubjects(models.Model):
    code = models.AutoField(primary_key = True)
    class_name = models.ForeignKey(Classes, on_delete = models.CASCADE)
    subject_name = models.ForeignKey(Subjects, on_delete = models.CASCADE)
    def __str__(self):
        return '{}. {}'.format(str(self.class_name), str(self.subject_name))
    
