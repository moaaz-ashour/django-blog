from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        # instantiate form with post data
        form = UserRegisterForm(request.POST)
        # validate the form when submitted
        if form.is_valid():
            # save User if form is valid
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created. You can log in now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')