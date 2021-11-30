from django.forms import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


@login_required
def home(request):
    photos = models.Photo.objects.all()
    return render(request, 'flux/home.html', context={'photos':photos})

@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')

    return render(request, 'flux/photo_upload.html', context={'form':form})