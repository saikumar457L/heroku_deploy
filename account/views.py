from django.shortcuts import render,get_object_or_404
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm,UserEditForm,ProfileEditForm

from .models import Profile,Marktry
from django.contrib import messages
# Create your views here.


@login_required
def dashboard(request):

    return render(request,"account/dashboard.html" ,{"section":"dashboard"})

def new_user(request):

    if request.method == "POST":

        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # create a new user
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)

            return render(request,"logins/register_done.html",{"new_user":new_user})

    else:
        user_form = UserRegistrationForm()

    return render(request,"logins/register.html",{"user_form":user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user,data=request.POST)

        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Profile update success")
        else:
            messages.error(request,"Profile update field.")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request,"account/edit.html",{"user_form":user_form,"profile_form":profile_form})


def just_try(request):
    post = Marktry.objects.all()
    return render(request,"site/try.html",{"posts":post})
