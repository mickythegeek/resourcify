from django.shortcuts import render
from .models import Post
# from . import views

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts" : posts})



def post_single(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post_single.html', {"posts" : posts})
