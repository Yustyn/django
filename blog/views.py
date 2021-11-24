from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from django.utils import timezone
from blog import *
from .forms import PostForm

# GET METHOD


def post_list(request):
    posts = Post.objects.filter(
        publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_lists.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# POST METHOD
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


# UPDATE METHOD
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'pk': pk})


# DELETE METHOD
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    posts = Post.objects.filter(
        publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_lists.html', {'posts': posts})
