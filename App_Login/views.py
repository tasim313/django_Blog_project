from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .Sign_up_forms import SignUpForm, UserProfileChange, UserProfilePic
from .models import UserProfile
# Create your views here.


def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    diction = {'form': form, 'registered': registered}
    return render(request, 'App_Login/sign_up.html', context=diction)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_Login/login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))


@login_required
def profile(request):
    return render(request,'App_Login/profile.html', context={})

@login_required
def profile_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(request.POST, instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    dict = {'form': form}
    return render(request, 'App_Login/change_profile.html', context=dict)


@login_required
def user_password_change(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    changed = False
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'App_Login/change_password.html', context={'form': form, 'changed': changed})

@login_required
def add_profile_pic(request):
    form = UserProfilePic()
    if request.method == 'POST':
        form = UserProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/profile_pic_add.html', context={'form': form})

@login_required
def change_profile_pic(request):
    form = UserProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = UserProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/profile_pic_add.html', context={'form': form})