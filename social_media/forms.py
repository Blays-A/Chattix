from django import forms
from .models import Comment , Video

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text' ]


class NewVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title' , 'caption' , 'img' , 'video' , 'slug']