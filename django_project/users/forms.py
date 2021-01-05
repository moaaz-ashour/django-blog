from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# a form which inherits from UserCreationForm
# use this form in the view instead of the UserCreationForm

STATES = (
    ('', 'Choose...'),
    ('BY', 'Bayern'),
    ('BE', 'Berlin'),
    ('BB', 'Brandenburg'),
    ('HB', 'Bremen'),
    ('HH', 'Hamburg'),
    ('NW', 'North Rhine-Westphalia')
)
class UserRegisterForm(UserCreationForm):
    # add email field
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    
    class Meta:
        # specify the model you want the form to interact with
        model = User
        # order of fields to be displayed in the form
        fields = ['username', 'email', 'password1', 'password2', 'city', 'state', 'zip_code']
        