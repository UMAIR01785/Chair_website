from django.shortcuts import render,redirect,get_object_or_404
from . models import Blog
from . forms import BlogForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def blog(request):
    blog=Blog.objects.all()
    context={
        'blog':blog,
    }
    return render(request,'blog/blog.html',context)


def detail_blog(request,slug):
    blog=Blog.objects.get(slug=slug)

    context={
        'blog':blog,
    }
    return render(request,'blog/detail_blog.html',context)

@login_required(login_url='login')
def blog_cart(request):
    blog=Blog.objects.filter(user=request.user).order_by('-created_at')
    context={
        'blog':blog
    }
    return render(request,'blog/blog_all.html',context)

def edit_blog(request,slug):
    blog=get_object_or_404(Blog,slug=slug)
    if request.method == "POST":
        form=BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_cart') 
        
    else:
        form=BlogForm(instance=blog)

    context={
        'form':form
    }


    return render(request,'blog/edit_blog.html',context)

def add_blog(request):
    if request.method == "POST":
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect('blog_cart')
    else:
        form= BlogForm()
    context={
        'form':form
    }
    return render(request,'blog/add_blog.html',context)


def delete_blog(request,slug):
    blog=get_object_or_404(Blog ,slug=slug)
    blog.delete()
    return redirect('blog_cart')


