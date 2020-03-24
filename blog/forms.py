from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    author=forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        'class':'textinputclass'
    }))
    text=forms.Textarea(attrs={
        'class':'editable medium-editor-textarea postcontent'
    })
    class Meta:
        model=Post
        fields=['author','title','text']


class CommentForm(forms.ModelForm):
    author=forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        'class':'textinputclass'
    }))
    text=forms.Textarea(attrs={
        'class':'editable medium-editor-textarea postcontent'
    })

    class Meta:
        model=Comment
        fields=['author','text']
