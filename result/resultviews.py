from django.shortcuts import render , get_object_or_404 , get_list_or_404 , redirect
from exam.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only



@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher','Student','Parent'])
def ManageTeacherClassStudentResultView(ResultView,id,pk):
    user = ResultView.user.groups.values('name')
    clas = get_object_or_404(TeacherClass , pk = id)
    student = get_object_or_404(TeacherClassStudents,pk = pk)
    tpercentage = '0'
    fmarks = '0'
    tmarks = '0'
    obtained = []
    subjects = []
    total = []
    numbers = []
    grade = ''
    k = '0'
    for i in Subjects.objects.all():
        if i not in subjects:
            subjects.append(i)
    for s in subjects:
        total_marks = '0'
        for d in ExamQuestions.objects.all():
            if str(student.clas.clas) == str(d.exam.class_name):
                if str(d.exam.subject) == str(s):
                    total_marks = int(total_marks) + int(d.marks)
        total.append({'subject':s.subject_name,'marks':total_marks})
    for i in subjects:
        obtained_marks = '0'
        for q in QuestionsChecked.objects.all():
            if str(clas.teacher) == str(q.student.clas.teacher):
                if str(q.student.pk) == str(student.pk):
                    if str(q.question.exam.subject) == str(i):
                        obtained_marks = int(obtained_marks) + int(q.obtained)
        obtained.append({'subject':i.subject_name,'marks':obtained_marks})
    for g in total:
        t = (total[int(k)])
        o = (obtained[int(k)])
        if str(t.get('subject')) == str(o.get('subject')):
            tmarks = int(tmarks) + int(t.get('marks'))
            fmarks = int(fmarks) + int(o.get('marks'))
            percentage = str(int(o.get('marks'))*100/int(t.get('marks')))
            numbers.append([t.get('subject'),t.get('marks'),o.get('marks'),percentage[:5]])
            k = int(k)+1
    tpercentage = str(int(tpercentage) + (int(fmarks)*100/int(tmarks)))[:5]
    if str(tpercentage) >= '80':
        grade = 'A+ Very Good'
    if str(tpercentage) >= '70' and str(tpercentage) <= '80':
        grade = 'A Good'
    if str(tpercentage) >= '60' and str(tpercentage) <= '70':
        grade = 'B Not Bad'
    if str(tpercentage) >= '50' and str(tpercentage) <= '60':
        grade = 'C'
    if str(tpercentage) <= '50':
        grade = "Failed"
    context = {
        'grade': grade ,
        'total_percentage': tpercentage ,
        'total_marks': tmarks ,
        'final_marks': fmarks ,
        'numbers': numbers ,
        'student': student ,
        'user': user ,
    }
    return render(ResultView , 'Result/Student.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher'])
def ManageTeacherClassResultView(ResultView,id):
    user = ResultView.user.groups.values('name')
    clas = get_object_or_404(TeacherClass, pk = id)
    students = get_list_or_404(TeacherClassStudents,clas = clas.pk)
    all = []
    rank = []
    for stu in students:
        tpercentage = '0'
        fmarks = '0'
        tmarks = '0'
        obtained = []
        subjects = []
        total = []
        numbers = []
        grade = ''
        k = '0'
        for sub in Subjects.objects.all():
            if sub not in subjects:
                subjects.append(sub)
        for subj in subjects:
            total_marks = '0'
            for d in ExamQuestions.objects.all():
                if str(stu.clas.clas) == str(d.exam.class_name):
                    if str(d.exam.subject) == str(subj):
                        total_marks = int(total_marks) + int(d.marks)
            total.append([subj.subject_name,total_marks])
            obtained_marks = '0'
            for q in QuestionsChecked.objects.all():
                if str(clas.teacher) == str(q.student.clas.teacher):
                    if str(q.student.pk) == str(stu.pk):
                        if str(q.question.exam.subject) == str(subj):
                            obtained_marks = int(obtained_marks) + int(q.obtained)
            obtained.append([subj.subject_name,obtained_marks])
            # print(obtained_marks)
        for g in total:
            t = (total[int(k)])
            o = (obtained[int(k)])
            if str(t[0]) == str(o[0]):
                to = '0'
                tmarks = int(tmarks) + int(t[1])
                fmarks = int(fmarks) + int(o[1])
                percentage = str(int(o[1])*100/int(t[1]))
                numbers.append({'subject':t[0],'total':t[1],'obtained':o[1],'percent':percentage[:5]})
                k = int(k)+1
                to = int(to) + int(fmarks)
        rank.append(to)
        tpercentage = str(int(tpercentage) + (int(fmarks)*100/int(tmarks)))[:5]
        if str(tpercentage) >= '80':
            grade = 'A+'
        if str(tpercentage) >= '70' and str(tpercentage) <= '80':
            grade = 'A'
        if str(tpercentage) >= '60' and str(tpercentage) <= '70':
            grade = 'B'
        if str(tpercentage) >= '50' and str(tpercentage) <= '60':
            grade = 'C'
        if str(tpercentage) <= '50':
            grade = "Failed"
        all.append({'name':stu.name,'father':stu.father_name,'numbers':numbers,'perc':tpercentage,'grade':grade})
    x = '0'
    for i in rank:
        x = int(x)+1
    for i in range(0,int(x)):
        v = max(rank)
        rank.remove(v)
    context = {
        'subjects': subjects ,
        'result': all ,
        'user': user ,
    }
    return render(ResultView,'Result/Class.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Teacher','Student','Parent'])
def ManageTeacherClassStudentResultAnswersView(AnswersView,exam,student):
    user = AnswersView.user.groups.values('name')
    data = []
    ans = []
    exam = get_object_or_404(ExamStatus , pk = exam)
    student = get_object_or_404(TeacherClassStudents , pk = student)
    for i in ExamAnswers.objects.all():
        if str(i.student.pk) == str(student.pk):
            if str(i.exam.pk) == str(exam.pk):
                ans.append(str(i.picture)[7:])
                d = {'name' : i.student.name ,'class' : i.student.clas.clas ,'teacher' : i.student.clas.teacher ,'subject' : i.exam.subject}
                if d not in data:
                    data.append(d)
    context = {
        'data': data ,
        'ans': ans ,
        'user': user ,
    }
    return render(AnswersView,'Result/StudentAnswers.html',context)
