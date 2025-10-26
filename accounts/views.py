from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            # Save user
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Save profile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Registration successful!')
            return redirect('register')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form})




@login_required(login_url='login')
def dashboard(request):
    user_profile = request.user.userprofile  # get the profile
    return render(request, 'accounts/dashboard.html', {'user_profile': user_profile})