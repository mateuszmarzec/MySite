from django import forms

from BlogAPI.models.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'text': forms.Textarea
        }
