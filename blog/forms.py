from .models import Comment
from django import forms  # from django-crispy-forms


class CommentForm(forms.ModelForm):
    """
    Class that inherits from the django base form
    """

    class Meta:
        """
        Telling CommentForm what model to use and
        then which fields we want displayed on our form
        """
        model = Comment
        fields = ('body',)  # , is important here to define it as a 'tuple' not a 'string'
