from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user
    posts = Post.objects.filter(user=user).order_by('-created_at')
    post_form = PostForm()

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = user
            post.save()
            return redirect('profile')

    return render(request, 'django_profile/profile.html', {'user': user, 'posts': posts, 'post_form': post_form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    return redirect('profile')
