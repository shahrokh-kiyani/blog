from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound

from .models import *
from .forms import CommentForm


class ListView(generic.ListView):
    # Paginate for items per page
    paginate_by = 4
    # Model post in models.py in blog app
    model = Post
    # Tepmlate name in tepmlates/blog/home.html
    template_name = 'blog/home.html'
    # Context name for template
    context_object_name = 'posts'


def post_detail_view(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        new_comment = comment_form.save(commit=False)
        new_comment.name = request.user
        new_comment.post = post
        new_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': comment_form,
    }
    print(context['comments'])
    print(context['post'])
    return render(request, 'blog/blog_single.html', context)

    

# category list view show all category's in site
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
        # We give name to input in template and we catch it here
        searched = request.POST['searched']
        # Here we check if user input was nothing we redierct him to 404 page
        if searched == '':
            return render(request, 'pages/404.html')

        # Here we search database for user search
        post = Post.objects.filter(title__contains=searched)

        # if the post user searched for not found will see 404 html
        if not post:
            return HttpResponseNotFound(render(request, 'pages/404.html'))

        context = {
            'searched': searched,
            'posts': post
        } 

        return render(request, 'blog/search.html', context)

    else: 
        return render(request, 'pages/404.html')
