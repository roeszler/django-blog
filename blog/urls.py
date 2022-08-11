from . import views
from django.urls import path


# create urlpatterns as a list
urlpatterns = [
    # as we are using views, we need to use as_views on the end of the PostList to render the class as a view
    path('', views.PostList.as_view(), name='home'),  # blank path indicates its our default home page

    # First slug is a path converter - converts this text into a slug field, 
    # It tells Django to match any slug string (ASCII characters or numbers, hyphens, underscores)
    # Second slug is a keyword name that matches the 'slug' input parameter in the 'get'
    # function within the PostDetail class within views.py file. 
    # Creating friendly URLs that consist of our Heroku project URL followed by the slug
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
