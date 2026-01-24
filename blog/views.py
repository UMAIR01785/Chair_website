from django.shortcuts import render
from . models import Blog
from . forms import BlogForm
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


