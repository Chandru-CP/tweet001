from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'hashtags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Write your post here...',
        })
        self.fields['hashtags'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add hashtags separated by commas...',
        })