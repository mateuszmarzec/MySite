from django.db import models
from django.utils.timezone import now


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tagi'

    def __str__(self):
        return '{}'.format(self.name)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(primary_key=True)
    tags = models.ManyToManyField(Tag)
    create_time = models.DateTimeField(default=now())
    release_time = models.DateTimeField(default=now())
    text = models.CharField(max_length=2000)
    thumbnail = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-create_time']
        verbose_name = 'Post'
        verbose_name_plural = 'Posty'

    def __str__(self):
        return '{} {}'.format(self.title, self.slug)
