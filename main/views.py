from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def portfolio(request):
    posts = Post.objects.filter().order_by('-created_date')
    for post in posts:
        print(post.id)
        print(post.title)
        print(post.pk)
        print(dir(posts[0]))
    return render(request, 'main/portfolio.html', {'posts':posts})

def contacts(request):
    return render(request, 'main/contacts.html')    