from .models import Comment
from django import forms # type: ignore

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)