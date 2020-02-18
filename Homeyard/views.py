from django.shortcuts import render, redirect
from .form import UserForm, UserProfileInfoForm

# login imports
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from Enquiry.form import UserEnquiryForm


def index(request):

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

    return render(request, 'Homeyard_html/index.html', {'user_form': user_enquiry})


def homeyard(request):

    return render(request, 'Homeyard_html/Welcome.html', {})


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'Homeyard_html/Registration.html', {'user_form': user_form,
                                                               'profile_form': profile_form,
                                                               'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'Homeyard_html/Welcome.html', {})


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'Homeyard_html/Welcome.html', {}) # HttpResponseRedirect(reverse('homeyard'))
            else:
                HttpResponse('Account is not active')
        else:
            print('Someone is tried to login and failed')
            print("Username:{} and password: {}" .format(username, password))
            return HttpResponse("invalid login details supplied")

    else:
        return render(request, 'Homeyard_html/Login.html', {})

