from django import forms
from . import models


class FollowersForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ['follower', 'following']
