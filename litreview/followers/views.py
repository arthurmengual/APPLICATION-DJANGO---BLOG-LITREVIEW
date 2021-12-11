from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from authentication import models


@login_required
def followers(request):
    actual_user = request.user
    follows = actual_user.follows
    if request.method == 'POST':
        search = request.POST['username']
        user = models.User.objects.filter(user__username__icontains=search)
        actual_user.follows.add(user.id)
        actual_user.save()
        return redirect('followers')

    return render(request, 'followers/followers.html', context={'follows': follows})
