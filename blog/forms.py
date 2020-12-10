from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Your blog title'}),
            'author': forms.Select(attrs={'class': 'form-control',
                                            'placeholder': 'Who are you?'}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                            'placeholder': 'Create here: '}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
