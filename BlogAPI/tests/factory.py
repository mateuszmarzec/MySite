import factory

from BlogAPI.models.models import Post, Tag


class TagFactory(factory.DjangoModelFactory):
    class Meta:
        model = Tag

    name = 'test_name'


class PostFactory(factory.DjangoModelFactory):
    class Meta:
        model = Post

    title = 'test_title'
    slug = 'test-slug'
    text = 'test_text'

    @factory.post_generation
    def set_tags(self, *args, **kwargs):
        self.tags.set(Tag.objects.all())
