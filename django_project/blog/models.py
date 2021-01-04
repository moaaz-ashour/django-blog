from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User,on_delete=models.CASCADE) if user deleted, their post will also be deleted
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
