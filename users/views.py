import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from bookpr.settings import EMAIL_HOST_USER
from users.forms import LoginForm
from users.models import UserConfirmationModel


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('books:list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            if send_confirmation_email(form.cleaned_data['email']):
                return render(request, 'conf.html')
            else:
                return redirect('books:list')
        else:
            return HttpResponse(form.errors)
    else:
        return render(request, 'signup.html')


def send_confirmation_email(email):
    subject = 'Confirmation email'
    code = random.randint(1000, 9999)
    if UserConfirmationModel.objects.filter(code=code).exists():
        send_confirmation_email(email)
    emails = [email]
    from_email = EMAIL_HOST_USER
    if send_confirmation_email(subject=subject, message=str(code), from_email=from_email, recipient_list=emails):
        UserConfirmationModel.objects.create(
            code=code,
            email=email,
            is_active=True

        )
        return True
    else:
        return False


def conf_view(request):
    if request.method == 'POST':
        code = request.post.get('code')
        user_code = UserConfirmationModel.objects.get(code=code)
        if user_code:
            user = User.objects.get(email=user_code.email)
            user.is_active = True
            user.save()
            return redirect('user:login')
        else:
            return redirect('books:list')
    else:
        return render(request, 'conf.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('user:login')
