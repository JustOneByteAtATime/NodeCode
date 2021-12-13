from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):

    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('comment',)


