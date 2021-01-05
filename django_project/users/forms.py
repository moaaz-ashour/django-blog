from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# a form which inherits from UserCreationForm
# use this form in the view instead of the UserCreationForm

class UserRegisterForm(UserCreationForm):
    # add email field
    email = forms.EmailField()
    
    class Meta:
        # specify the model you want the form to interact with
        model = User
        # order of fields to be displayed in the form
        fields = ['username', 'email', 'password1', 'password2']
        