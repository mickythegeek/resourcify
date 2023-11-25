from django.shortcuts import render
from .models import Post
# from . import views

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts" : posts})



def post_single(request):
    return render(request, 'post_single.html')
