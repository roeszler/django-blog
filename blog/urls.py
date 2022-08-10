from . import views
from django.urls import path


# create list
urlpatterns = [
    # as we are using views, we need to use as_views on the end of the PostList to render the class as a view
    path('', views.PostList.as_view(), name='home')  # blank path indicates its our default home page
]
