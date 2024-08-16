from django import forms
from django.forms import ModelForm
from users.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("username_graduate", "username_author", "text")
