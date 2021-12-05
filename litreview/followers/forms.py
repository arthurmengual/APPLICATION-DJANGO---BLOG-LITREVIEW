from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class FollowersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']