from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm

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
    Creates and Retrieves the detail view of a particular blog post
    """

    def get(self, request, slug, *args, **kwargs):  # define the function and inputs
        """
        Retrieves information for display in each blog post
        """
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
                'commented': False,  # indicates that the post has not been commented on
                'liked': liked,

                # to render the form as part of our view:
                'comment_form' : CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        """
        Creates information in each blog post
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)  # this will get all of the data that we posted from our form.

        if comment_form.is_valid():
            """
            The form has a method called 'is_valid' that returns a Boolean value
            regarding whether the form is valid. If it is valid, a comment has been
            left and we want to process it.
            """
            comment_form.instance.email = request.user.email  # set our email and our username automatically from the logged in user
            comment_form.instance.name = request.user.name
            comment = comment_form.save(commit=False)  # not committing it just yet, as we need to first assign a post to it.
            comment.post = post  # assign the post to the comment
            comment.save()  # now save the post with comment attached
        else:  # if the form is not valid then we just want to return an empty comment form instance
            comment_form = CommentForm()
        
        # Now to send all of this above information to our render method:
        return render(
            request,  # send request
            'post_detail.html',  # supply template we require
            # dictionary to supply context:
            {
                'post': post,
                'comments': comments,
                'commented': True,  # indicates that the post has been commented on
                'liked': liked,

                # to render the form as part of our view:
                'comment_form' : CommentForm()
            },
        )
