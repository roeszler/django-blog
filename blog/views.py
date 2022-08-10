from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

class PostList(generic.ListView):
    """
    Built-in class-based generic view from Django to 
    quickly render the list view of the blog posts
    """
    model = Post  # use post as the classes model
    queryset = Post.objects.filter(status=1).order_by('-created_on')  # status 0 = draft, 1 = published
    template_name = 'index.html'
    paginate_by = 6  # separate and limit to display 6 posts, or add page navigation


# Class-based views are different. Instead of using an if statement to check the request method,  
# we simply create class methods called get or post, or any other HTTP verb.
class PostDetail(View):
    """
    Creates the detail view of a particular blog post.
    """

    def get(self, request, slug, *args, **kwargs):  # define the function and inputs
        queryset = Post.objects.filter(status=1)  # only active posts
        post = get_object_or_404(queryset, slug=slug)  # get object or alternately 404
        comments = post.comments.filter(approved=True).order_by('created_on')  # to get any comments that are attached to the post
        liked = False  # default liked status
        if post.likes.filter(id=self.request.user.id).exists(): # to see if the logged in user has liked this post or not
            liked = True
        
        # Now to send all of this above information to our render method:
        return render(
            request,  # send request
            'post_detail.html',  # supply template we require
            # dictionary to supply context:
            {
                'post': post,
                'comments': comments,
                'liked': liked
            },
        )
