from django import forms
from models import Massage
class PostForm(forms.Form):
    title = forms.CharField(max_length=255)

class PostModelForm(forms.ModelForm):
    title = forms.CharField(max_length=255)

    class Meta:
        model = Massage
        exclude = ['parent']