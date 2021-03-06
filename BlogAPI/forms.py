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
            'agreement': 'Wyrażam zgodę na przechowywanie wprowadzanych danych osobowych w celu wysyłania Newslettera.',
        }
        error_messages = {
            'email': {
                'required': 'To pole jest wymagane.',
            },
        }
        help_texts = {
            'first_name': 'Podanie imienia nie jest obowiązkowe.',
            'email': 'Email na który wysyłany ma być Newsletter.',
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            NewsletterParticipant.objects.get(email=email)
            raise forms.ValidationError('Ten email jest już zapisany na Newsletter.')
        except NewsletterParticipant.DoesNotExist:
            pass
        return email

    def clean_agreement(self):
        agreement = self.cleaned_data['agreement']
        if not agreement:
            raise forms.ValidationError('Musisz wyrazić zgodę na przetwarzanie danych.')
        return agreement
