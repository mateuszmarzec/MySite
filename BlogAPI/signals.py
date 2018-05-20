# coding=utf-8
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from BlogAPI.models.models import Post, NewsletterParticipant
from MySite.settings.settings import EMAIL_HOST_USER


EMAIL = {
    'title': 'Dodano nowy post!',
    'body': 'Dodano post o tytule {}, zapraszamy do przeczytania pod linkiem : https://peaceful-castle-35594.herokuapp.com/post/{}',
}


@receiver(post_save, sender=Post)
def send_newsletter_email(sender, instance, **kwargs):

    participants_list = [p.email for p in NewsletterParticipant.objects.all()]
    send_mail(
        EMAIL['title'],
        EMAIL['body'].format(instance.title, instance.slug),
        EMAIL_HOST_USER,
        participants_list,
    )
