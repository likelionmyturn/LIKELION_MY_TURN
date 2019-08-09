from django import forms
from .models import Number

class PostForm(forms.ModelForm):

    class Meta:
        model = Number
        fields = ('num',)