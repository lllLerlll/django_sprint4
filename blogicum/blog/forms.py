from django import forms
from .models import Post, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'location', 'category', 'image')
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class ProfileEditForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')
