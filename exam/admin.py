from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ExamStatus)
admin.site.register(ExamQuestions)
admin.site.register(ExamAnswers)
admin.site.register(QuestionsChecked)
admin.site.register(Guide)