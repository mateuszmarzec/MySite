from django import forms

from BlogAPI.models.models import Post, NewsletterParticipant


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'text': forms.Textarea
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterParticipant
        exclude = ('create_time',)
        labels = {
            'first_name': 'Imię',
            'email': 'Email',
            'agreement':  'Wyrażam zgodę na przechowywanie wprowadzanych danych osobowych w celu wysyłania Newslettera'
        }
