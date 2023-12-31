from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text", "author",]
        labels = {
            "text": "Your comment",
            "author": "Your name",
        }
