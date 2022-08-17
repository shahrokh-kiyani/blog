from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import *


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

    queryset = Post.objects.all()
    

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

# Category detail view show all posts have same category
def category_detail_view(request, slug):
    # Find category and post in database
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category)
    # Context send for template
    context = {
        'category': category,
        'posts': posts
    }

    return render(request, 'blog/category_detail.html', context)


# This is search view that will search around all database to found a user input
def search_view(request):

    if request.method == 'POST':
        searched = request.POST['searched']
        # Here we check if user input was nothing we redierct him to 404 page
        if searched == '':
            return render(request, 'pages/404.html')

        # Here we search database for user search
        post = Post.objects.filter(title__contains=searched)
        
        context = {
            'searched': searched,
            'posts': post
        } 

        return render(request, 'blog/search.html', context)

    else: 
        return render(request, 'pages/404.html')
