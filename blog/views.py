from django.shortcuts import render
from django.views import generic

from .models import Post

class ListView(generic.ListView):
    paginate_by = 3
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/blog_single.html'
    context_object_name = 'post' 
    