from typing import Literal
from django.contrib.auth import login
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from .models import UserFollows
from django.contrib import messages


@login_required
def followers(request):
    followed = UserFollows.objects.filter(
        following__exact=request.user)
    followers = UserFollows.objects.filter(
        follower__exact=request.user)
    if request.method == 'POST':
        try:
            search = request.POST['username']
            user = get_object_or_404(User, username__exact=search)
            follower = UserFollows(follower=request.user, following=user)
            follower.save()
            return redirect('followers')
        except:
            messages.error(
                request, "Cette utilisateur n'existe pas, veuillez réessayer")
            return redirect('followers')

    return render(request, 'followers/followers.html', context={'followed': followed, 'followers': followers})


@login_required
def unfollow(request, user_id):
    follow = UserFollows.objects.filter(
        following__exact=user_id).filter(follower__exact=request.user)
    follow.delete()
    return redirect('followers')
