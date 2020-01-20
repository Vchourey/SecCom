from django.shortcuts import render, redirect
import datetime
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.http import HttpResponse
from Mylearning.models import Topic, Reading_Material, Interview_QA
from Mylearning import forms
from Mylearning.forms import StudentRegForm
from django.views.generic import View, ListView, DetailView, TemplateView


today = datetime.datetime.now().date()
Current_time = datetime.datetime.now().time()

select_topic = Topic.objects.all()


def Mylearning(request):

    if request.method == "POST":

        return InterviewQuestion(request)

    return render(request, "learning-html/welcome.html", {"today": today, "timenow": Current_time, "select_topics": select_topic})


def InterviewQuestion(request):

    return render(request, 'learning-html/interview.html', {"today": today, "timenow": Current_time, "select_topics": select_topic})

'''
def InterviewQuestionAnswer(request):

    return render(request, 'learning-html/interviewQA.html', {"today": today, "timenow": Current_time, "select_topics": select_topic})
#    return redirect(InterviewQuestion)
'''

class InterviewQuestionAnswer(ListView):
    context_object_name = 'questions'
    model = Topic
    template_name = 'learning-html/interviewQA.html'


def simplemail(emailto):

    resp = send_mail(subject="Question Status", message="you have successfully vjhcc uploaded question ", from_email="TechLearn@vijay.com",
                     recipient_list=[emailto], fail_silently=True, connection='django.core.mail.backends.smtp.EmailBackend')
    return HttpResponse('$s', resp)

# simplemail('vijaychourey26@gmail.com')

def bulkmail(emailto):

    msg1=('test1', 'testing bulk mail', 'vijaychourey26@gmail.com', [emailto[0]])
    msg2=('test1', 'testing bulk mail', 'vijaychourey26@gmail.com', [emailto[1]])
    res = send_mass_mail((msg1, msg2), fail_silently=False, connection='django.core.mail.backends.smtp.EmailBackend')
    return HttpResponse('%s'%res)
mem =('vijaychourey26@gmail.com', 'vijaychourey@outlook.com')
# bulkmail(mem)


def StudentReg(request):

    regform = StudentRegForm()

    if request.method == "POST":
        regform = StudentRegForm(request.POST)

        if regform.is_valid():
            regform.save(commit=True)
            return Mylearning(request)
        else:
            print('Form is invalid')

    return render(request, 'learning-html/regform.html', {'form': regform})

