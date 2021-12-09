from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from authentication import models


@login_required
def followers(request):
    actual_user = request.user
    follows = actual_user.follows
    if request.method == 'POST':
        search = request.POST['username']
        users = models.User.objects.all()
        for user in users:
            if user.username == search:
                if user.username != request.user.username:
                    actual_user.follows.add(user)
                    actual_user.save()
                    return redirect('followers')

    return render(request, 'followers/followers.html', context={'follows': follows})
