from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        # instantiate form with post data
        form = UserRegisterForm(request.POST)
        # validate the form when submitted
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})