from django.db import models


class Post(models.Model):
    message = models.TextField()
    hashtags = models.CharField(max_length=100)
    user = models.ForeignKey('django_accounts.UserProfile', on_delete=models.CASCADE)
