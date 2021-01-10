from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
    """
        a form which inherits from UserCreationForm
        use this form in the view instead of the UserCreationForm
    """
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    
    class Meta:
        # specify the model you want the form to interact with
        model = User
        # order of fields to be displayed in the form
        fields = ['username', 'email', 'password1', 'password2', 'city', 'state', 'zip_code']


class UserUpdateForm(forms.ModelForm):
    """
        A form which updates our User model.
        Model Form: allows to create a form which works with a specific database model.
        # We want to update the username and email only.
    """
    username = forms.Field(label='username', widget=forms.TextInput(attrs={'placeholder': 'Enter new username'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter new email'}))
    class Meta:
        # specify the model you want the form to interact with
        model = User
        # order of fields to be displayed in the form
        fields = ['username', 'email']
