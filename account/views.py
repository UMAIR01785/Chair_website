from django.shortcuts import render,redirect
from . forms import RegisterForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from . forms import ProfileForm
from django.contrib.auth.models import User
from .models import Profile
from blog.models import Blog


# Create your views here.
def register(request):
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            auth.login(request ,user)
            return redirect('home')
    else:
        form=RegisterForm()
    
    context={
        'form':form
    }

    return render(request,'account/register.html',context)


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(request,username=username,password=password)
        if user is not None:
         auth.login(request ,user)
         return redirect('home')
        else:
         return redirect('register')
    return render(request,'account/login.html')
  
    
    
    
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
   blog=Blog.objects.all()
   count=blog.count()
   user=request.user
   context={
       'user':user,
       'count':count
   }
   return render(request,'account/dashboard.html',context)

@login_required(login_url='login')
def profile(request):
    profile , created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form=ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
          form=ProfileForm(instance=profile)
    context={
        'form':form
    }
          
    return render(request,'account/profile_mange.html',context)
        
   



