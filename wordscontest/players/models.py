from django.db import models

from .servises import get_avatars_path


class Achievement(models.Model):
    name = models.CharField(max_length=50)
    rare = models.PositiveSmallIntegerField(default=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    """
        Player's profile
    """
    nickname = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to=get_avatars_path, blank=True, null=True)
    score = models.PositiveIntegerField(blank=True, default=0)
    achievements = models.ManyToManyField(Achievement, related_name='players', blank=True)

    def __str__(self):
        return self.nickname


