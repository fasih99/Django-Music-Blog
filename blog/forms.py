from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text',)

        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control btn-success'}),
        'author': forms.Select(attrs={'class': 'form-control btn-success'}),
        'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
        #the widgets dict is for styling the fields of our forms
        #class editable and medium-editor-textarea are not our generic classes

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control loader'}),
            'text': forms.Textarea(attrs={'class': 'editable  medium-editor-textarea loader'}),
        }
