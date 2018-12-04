from django.shortcuts import render, redirect, reverse, get_object_or_404
from accounts.forms import loginForm, userRegisterForm, editProfile,bio_and_image
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from tickets.models import add_tickets_form
from .models import Profile
from django.utils import timezone
# Create your views here.
  
def index(request):
    tickets = add_tickets_form.objects.all()
    print(tickets)
    return render(request,'index.html', {'tickets':tickets})

def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
       form = loginForm(request.POST)
       
       if form.is_valid():
           user = auth.authenticate(username = request.POST['username'],
                                    password = request.POST['password'] )
           
           
           if user:
               auth.login(user=user, request=request)
               messages.success(request, 'you successfully logged in')
               return redirect(reverse('index'))
           else:
               form.add_error(None,'your password or username is incorrect')
    else:
        form = loginForm()
    return render(request,'login.html',{"form":form})
    
def user_register(request):
    if request.method == "POST":
        registration_form = userRegisterForm(request.POST)
    
        if registration_form.is_valid():
           registration_form.save()
           user = auth.authenticate(username = request.POST['username'],
                                    password = request.POST['password1'] )
           if user:
            auth.login(user=user, request=request)
            messages.success(request, 'you successfully logged in')
            return redirect(reverse('index'))
           else:
            messages.error(request,'Unable to register at these time')
    else:    
       registration_form = userRegisterForm()
    return render(request,'register.html',{"registration_form":registration_form})
    
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,"You successfully logged out")
    return redirect(reverse('index'))
    
def profile(request, pk=None):
    profile = request.user.profile
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    return render(request,'user_profile.html', {'user':user})
@login_required    
def edit_user_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = editProfile(request.POST, request.FILES, instance=request.user) 
        bio_form = bio_and_image(request.POST, request.FILES, instance=profile)
        print(form)
        if form.is_valid() and bio_form.is_valid():
            form.save()
            bio_form.save()
            return redirect('profile')
    else:
        form = editProfile(instance=request.user)
        bio_form = bio_and_image(instance=profile)
    return render(request,'profile_edit.html',{"form":form, "bio_form":bio_form})

def changePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user) 
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('profile'))
        else:
            return redirect(reverse('editProfile'))
    else:
        form =PasswordChangeForm(user=request.user) 
    return render(request,'change_password.html',{"form":form})
    
    
    
    
    
    
    
    
    
    