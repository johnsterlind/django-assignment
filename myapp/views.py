from django.shortcuts import render

from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()  # Fetch all posts
    return render(request, 'home.html', {'posts': posts})
