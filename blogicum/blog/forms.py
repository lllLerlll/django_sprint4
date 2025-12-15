from django import forms
from .models import Post, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


class PostForm(forms.ModelForm):
    """Форма для создания и редактирования постов.
    Используется в PostCreateView и PostUpdateView."""

    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'location',
                  'category', 'image', 'is_published')
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'})
        }


class CommentForm(forms.ModelForm):
    """Форма добавления комментариев"""

    class Meta:
        model = Comment
        fields = ('text',)


class ProfileEditForm(UserChangeForm):
    """Форма для редактирования профиля пользователя.
    Наследуется от UserChangeForm"""

    password = None

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')
