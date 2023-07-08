from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import user_form,user_form1,post_form
from .models import user_model,post_model,User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
import datetime

# Create your views here.
def index(request):
    models=post_model.objects.all()
    umodel=user_model.objects.all()
    model=[]
    for i in models:
        model=[i]+model
    return render(request,'index.html',{'model':model,'umodel':umodel})

def createaccount(request):
    if request.method == 'POST':
        user_formA=user_form(request.POST)
        user_formB=user_form1(request.POST)
        if user_formA.is_valid() and user_formB.is_valid():
            formA=user_formA.save()
            formA.set_password(formA.password)
            formA.save()
            formB=user_formB.save(commit=False)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    formB.key = request.user
                    formB.formA=formA
                    formB.save()
                    return HttpResponseRedirect(reverse('blog_app:dashboard'))
    else:
        user_formA=user_form()
        user_formB=user_form1()
    return render(request,'createaccount.html',{'user_formA':user_formA,'user_formB':user_formB})

def dashboard(request):
    model=user_model.objects.all()
    return render(request,'dashboard.html',{'model':model})

def createpost(request):
    if request.method == 'POST':
        form=post_form(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            print(request.user)
            instance = form.save(commit=False)
            instance.user = request.user
            instance.date = datetime.datetime.now()
            instance.save()
        return redirect('blog_app:index')
    return render(request,'createpost.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            print(user)
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('blog_app:index'))
            else:
                return HttpResponse('User Not Active')
        else:
            return HttpResponse('Incorret Creds')

    return render(request,'login.html',)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog_app:index'))

def profiles(request):
    data=User.objects.all()
    data1=user_model.objects.all()
    return render(request,'profiles.html',{'data':data,'data1':data1})

def myprofile(request):
    models=post_model.objects.all().filter(user=request.user)
    model=[]
    for i in models:
        model=[i]+model
    umodel=user_model.objects.all()
    return render(request,'myprofile.html',{'model':model,'umodel':umodel})