from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    """
    Built-in class-based generic view from Django to 
    quickly render our posts
    """
    model = Post  # use post as the classes model
    queryset = Post.objects.filter(status=1).order_by('-created_on')  # status 0 = draft, 1 = published
    template_name = 'index.html'
    paginate_by = 6  # separate and limit to display 6 posts, or add page navigation
