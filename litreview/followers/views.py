from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms


@login_required
def followers(request):
    form = forms.FollowersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('followers')
    
    return render(request, 'followers/followers.html', context={'form': form})