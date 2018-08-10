from django.shortcuts import render
from . models import blogModel

# Create your views here.
def list_view(request):
    object_list = blogModel.objects.all()
    print("in list")
    context = {
            "list": object_list,
            "title" : "test"
        }
    return render(request, 'Blog/blog.html', context)

def post_view(request):
    print("in post")
    context = {
        "title" : "test"
        }
    return render(request, 'Blog/blog.html', context)

def create_view(request):
    return render(request, 'Blog/blog.html', context)

def update_view(request):
    return render(request, 'Blog/blog.html', context)

def delete_view(request):
    return render(request, 'Blog/blog.html', context)
