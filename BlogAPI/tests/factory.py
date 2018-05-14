from BlogAPI.models.models import Post, Tag
from factory.django import DjangoModelFactory


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post
        django_get_or_create = ('title', 'slug', 'tags', 'create_time', 'release_time', 'text',)


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag
        django_get_or_create = ('name',)
