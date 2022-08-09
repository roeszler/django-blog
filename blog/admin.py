from django.contrib import admin
from .models import Post, Comment

# To tell our admin panel which field we want to use Summernote WYSIWYG form for.
# ie our content field (stored as a text field in the database) is going to be a Summernote field. 

from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)  # decorator method
class PostAdmin(SummernoteModelAdmin):
    """
    Class to add content / function / configuration to the PostAdmin panel
    Will inherit from the imported SummernoteModelAdmin
    The content field / blog content (a Django text field) will use summernote
    The 'admin.site.register' method only allows us to pass in two arguments
    and it quickly gets full. 
    The 'decorator is a more Pythonic way to handle the registration.
    """
    list_display = ('title', 'slug', 'status', 'created_on')  # django included colum display
    search_fields = ['title', 'content']  # django included search bar
    prepopulated_fields = {'slug': ('title',)}  # prepopulated_fields property, specifically designed for generating slug fields.
    list_filter = ('status', 'created_on')  # django included side filter panel
    summernote_fields = ('content')  # from content defined in the Post model (table) in models.py

# admin.site.register(Post) # This method only allows us to pass in two arguments so it quickly gets full.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Class to add content / function / configuration to the CommentAdmin panel
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']  # to specify different actions that can be  performed from the action drop-down box.

    def approve_comments(self, request, queryset):
        """
        Function to call the update method on the query set and change our approved
        boolean field (set to false by default) to true!
        Queryset targeted to update the record
        """
        queryset.update(approved=True)
