from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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

@login_required
def profile(request):
    if request.method == 'POST':
        # instantiate user_update form with post data and User instance
        ua_form = UserUpdateForm(request.POST, instance=request.user)
        # instantiate profile_update form with post data, image and User instance
        pa_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if ua_form.is_valid() and pa_form.is_valid():
            ua_form.save()
            pa_form.save()
            messages.success(request, f'Account updated!')
            return redirect('profile')
    else:
        ua_form = UserUpdateForm(instance=request.user)
        pa_form = ProfileUpdateForm(instance=request.user.profile)         
    context = {
        'ua_form': ua_form,
        'pa_form': pa_form
    }
    return render(request, 'users/profile.html', context)