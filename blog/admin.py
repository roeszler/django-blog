from django.contrib import admin
from .models import Post

# To tell our admin panel which field we want to use Summernote WYSIWYG form for.
# ie our content field (stored as a text field in the database) is going to be a Summernote field. 

from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)  # decorator method
class PostAdmin(SummernoteModelAdmin):
    """
    Will inherit from the imported SummernoteModelAdmin
    and our content field / blog content (a Django text field), use summernote
    the below admin.site.register method only allows us to pass in two arguments
    so it quickly gets full. The above decorator is also a more Pythonic way to
    handle the registration.
    """
    summernote_fields = ('content')  # from content defined in the Post model (table) in models.py

# admin.site.register(Post) # This method only allows us to pass in two arguments so it quickly gets full.
