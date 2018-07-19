from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def list_of_post(request):
    post = Post.objects.all()
    template = 'blog/post/list_of_post.html'
    context = {'post': post}
    return render(request, template, context)

def post_detail(request, slug):
# def post_detail(request, id):
    post = get_object_or_404(Post, slug=slug)
    # post = get_object_or_404(Post, id=id)
    template = 'blog/post/post_detail.html'
    context = {'post': post}
    return render(request, template, context)