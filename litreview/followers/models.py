from django.db import models
from django.db.models.deletion import CASCADE
from authentication.models import User


class UserFollows(models.Model):
    following = models.ForeignKey(
        User, on_delete=CASCADE, blank=True, related_name="following")
    follower = models.ForeignKey(
        User, on_delete=CASCADE, blank=True, related_name="follower")

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ['following', 'follower']
