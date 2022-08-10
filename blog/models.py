from django.db import models
from django.contrib.auth.models import User  # import the user model
from cloudinary.models import CloudinaryField # import our Cloudinary field for the featured image

STATUS = ((0, 'Draft'), (1, 'Published'))  # a tuple (finite ordered list) for our published status

class Post(models.Model):
    """
    A 'table' that inherits from our standard model
    See relationship-diagram.png
    Defines the post model content to be read and updated
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  #  a foreign key relationship, one-to-many from our user model, cascade it to delete any subsequent attached foreign keys in other tables.
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    # helpers A couple of extra methods to our Posts model which can be considered as helpers
    # Ordering, Indexing and Constraints
    class Meta:
        """
        To order our posts in a descending '-' format 
        """
        ordering = ['-created_on']
    

    def __str__(self):
        """
        a magic method that returns a string representation of an object
        should define it because the default isn't helpful at all
        """
        return self.title
    

    def number_of_likes(self):
        """
        to return the total number of likes on a post
        """
        return self.likes.count()


class Comment(models.Model):
    """
    The model to define the content within the
    Comments 'table' to be read and updated
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        To order comments in a ascending format
        """
        ordering = ['created_on']
    
    def __str__(self):
        """
        to return the comment and author of comment on a post
        """
        return f'Comment {self.body} by {self.name}'
