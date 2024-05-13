import random
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog



# Create your views here.

def indexPage(request):
    blog_List = Blog.objects.all()
    return render(request, 'index.html', {'blogs':blog_List})

def add_blog(request):
    if request.method == 'POST':
        new_blog = request.POST

        blog_title = request.POST.get('blog_title')
        blog_text = request.POST.get('blog_text')
        blog_Img = request.FILES.get('blog_Img')

        Blog.objects.create(
            blog_title = blog_title,
            blog_text = blog_text,
            blog_Img = blog_Img
        )
        return redirect('indexPage')

    else:
        return render(request, 'add_blog.html')
    

def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog_title = request.POST.get('blog_title')
        blog_text = request.POST.get('blog_text')
        blog_Img = request.FILES.get('blog_Img')
 
        blog.blog_title = blog_title
        blog.blog_text = blog_text
        if blog_Img:
            blog.blog_Img = blog_Img
        blog.save()
        return redirect('indexPage')
    else:
        return render(request, 'edit_blog.html', {'blog': blog})

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('indexPage')
    else:
        return render(request, 'delete_blog.html', {'blog': blog})
    
def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'view_blog.html', {'blog': blog})

# def search_blog(request, blog_title):
#     blog_search = Blog.objects.filter(blog_title__contains=blog_title)
#     if request.method == 'POST':
#         return render(request, 'view_blog', {'blog_search': blog_search})
#     else:
#         return render(request, 'view_blog', {'blog_search': blog_search})
  