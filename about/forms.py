from .models import CollaborateRequest
from django import forms # type: ignore

class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')