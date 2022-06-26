from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from home.models import Category

def user_register(request):
    if request.method=='POST':
        form=userRegisterForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=User.objects.create_user(username=data['user_name'], email=data['email'], first_name=data['first_name'],last_name=data['last_name'], password=data['password2'])
            user.save()
            return redirect('home:main')
    else:
        form=userRegisterForm()
    category=Category.objects.filter(sub=False)
    context={'form':form,'category':category}
    return render(request,'accounts/register.html',context)

def user_login(request):
    if request.method == 'POST':
        form=userLoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'], password=data['password'])
            if user:
                login(request,user)
                request.session.set_expiry(0)
            return redirect('home:main')
    else:
        form=userLoginForm()
    category=Category.objects.filter(sub=False)
    context={'form':form,'category':category}
    return render(request,'accounts/login.html',context)

def user_logout(request):
    logout(request)
    return redirect("home:main")

@login_required(login_url='accounts:user_login')
def profile(request):
    profile=Profile.objects.get(user_id=request.user.id)
    category=Category.objects.filter(sub=False)
    context={'profile':profile,'category':category}
    return render(request,'accounts/profile.html',context)

@login_required(login_url='accounts:user_login')
def update(request):
    if request.method == 'POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('accounts:profile')
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)
    profile=Profile.objects.get(user_id=request.user.id)
    category=Category.objects.filter(sub=False)
    context={"user_form":user_form, 'profile_form':profile_form,"profile":profile,'category':category}
    return render(request,'accounts/update.html', context)

def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('accounts:profile')
        else:
            return redirect('accounts:change')
    else:
        form=PasswordChangeForm(request.user)
    profile=Profile.objects.get(user_id=request.user.id)
    category=Category.objects.filter(sub=False)
    context={'form':form,'profile':profile,'category':category}
    return render(request,'accounts/change_password.html',context)