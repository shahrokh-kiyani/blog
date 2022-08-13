from django.shortcuts import render
from django.views import generic

from .models import *


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
    

# category list view show all categorys in site
class CategoryListView(generic.ListView):
    # Paginate for categorys 
    paginate_by = 10
    # model category from models.py
    model = Category
    # template name in tepmlates/blog/category_list.html
    template_name = 'blog/category_list.html'
    # context name for template
    context_object_name = 'categories'


# Category Detail View show all posts related to category
class CategoryDetailView(generic.DetailView):
    # Model category from models.py
    model = Category
    # template name in tepmlates/blog/category_detail.html
    template_name = 'blog/category_detail.html'
    # context name for template
    context_object_name = 'category'

    def get