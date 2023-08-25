from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def homepage_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Assuming user is authenticated
            post.save()
            return render(request, 'django_homepage/homepage.html')
    else:
        form = PostForm()
    posts = Post.objects.all()
    return render(request, 'django_homepage/homepage.html', {'form': form, 'posts': posts})
