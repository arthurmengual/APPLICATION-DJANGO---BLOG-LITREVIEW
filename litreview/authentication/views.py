from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth import login
from django.conf import settings


def signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    
    return render(request, 'authentication/signup.html', context={'form':form})


def upload_profile_photo(request):
    form = forms.UploadProfilePhoto(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhoto(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'authentication/upload_profile_photo.html', context={'form':form})