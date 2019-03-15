from django import forms
from .models import Post
from django.contrib.auth.models import User

class P_Form(forms.ModelForm):
    invite = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Post
        fields = ['title', 'content', 'expdate', 'invite', 'private']
