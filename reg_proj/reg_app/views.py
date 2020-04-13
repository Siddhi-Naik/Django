from django.shortcuts import render
from .forms import UserProfileInfoForm,UserForm


from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    return render(request,'reg_app/index.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))    

def register(request):

    registered=False

    if request.method =='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True

        else:
            print(user_form.errors,profile_form.errors)    
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'reg_app/register.html',
    {'user_form':user_form,'profile_form':profile_form,
    'registered':registered})

def user_login(request):


    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return  HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('User seesion is not active')
        else:
            print("A unknown user happens to be logging in")
            print("Username:{} and Password:{}".format(username,password))
    else:  
         return render(request,'reg_app/login.html',{})         
       



    
