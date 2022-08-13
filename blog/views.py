from django.shortcuts import render
from django.views import generic

from .models import Post


#class ListView For home page
class ListView(generic.ListView):
    # Paginate for items per page
    paginate_by = 4
    # Model post in models.py in blog app
    model = Post
    # Tepmlate name in tepmlates/blog/home.html
    template_name = 'blog/home.html'
    # Context name for template
    context_object_name = 'posts'


# Class Detail View for each post
class DetailView(generic.DetailView):
    # Model post in models.py in blog app
    model = Post
    # Tepmlate name in tepmlates/blog/detail.html
    template_name = 'blog/blog_single.html'
    # Context name for template
    context_object_name = 'post' 
    