from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User,on_delete=models.CASCADE) if user deleted, their post will also be deleted
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # get_absolute_url()
    # If get_absolute_url is not defined, we will get an error:
    # ImproperlyConfigured at /post/new
    # No URL to redirect to. Either provide a url or define a get_absolute_url method on the Model.
    def get_absolute_url(self):
        """
            get_absolute_URL: a method to find the URL of a model Object, which returns the path to a specific instance

            - in our case, we need to return the URL as a string and let the view handle the the redirect for us.

            redirect(): redirects to a specific route
            reverse(): returns the full URL to that route as a string
        """
        # our url parameter is called 'pk' and its value should be the instance of a specific post
        return reverse('post-detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.title