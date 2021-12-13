from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from .models import UserFollows


@login_required
def followers(request):
    follower = UserFollows()
    user_following = get_object_or_404(UserFollows, follower=request.user)
    if request.method == 'POST':
        try:
            search = request.POST['username']
            user = get_object_or_404(User, username=search)
            follower = UserFollows(follower=request.user, following=user)
            follower.save()
            return redirect('followers')
        except:
            return HttpResponse('<h1>No user found, try again<h1/>')

    return render(request, 'followers/followers.html', context={'follow': user_following})
