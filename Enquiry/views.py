from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactDetail, Enquiry
from .form import UserEnquiryForm

'''
def Contact_Enquiry(request):

    try:
        list_contact = UserEnquiryForm.objects.all()

    except:
        return HttpResponse("error while reading database")

    return render(request, 'enquiry_html/contactpage.html', {"contact": list_contact})
'''

def Contact_Enquiry(request):

    user_enquiry = UserEnquiryForm()

    if request.method == "POST":

        enquiry = UserEnquiryForm(request.POST, request.FILES)

        if enquiry.is_valid():

            user_enq = enquiry.save(commit=False)

            try:
                user_enq.file = request.FILES['file']

            except:
                return render(request, 'enquiry_html/ThankYou.html', {})

            finally:
                user_enq.save()

        else:
            print(user_enquiry.errors)

        return render(request, 'enquiry_html/ThankYou.html', {})

    else:
        user_enquiry = UserEnquiryForm()

    try:
        list_contact = ContactDetail.objects.all()

    except:
        return HttpResponse("error while reading database")

    return render(request, 'enquiry_html/contactpage.html', {"contact": list_contact,
                                                             'user_form': user_enquiry})





def Thanks(request):

    return render(request, 'enquiry_html/ThankYou.html', {})

'''
def InterviewQuestionAnswer(request):

    return render(request, 'learning-html/interviewQA.html', {"today": today, "timenow": Current_time, "select_topics": select_topic})
    return redirect(InterviewQuestion)

'''