from django.test import Client, TestCase
from django.utils import timezone

from BlogAPI.tests import factory
from BlogAPI.models.models import Post


class BaseTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag = factory.TagFactory.create()
        self.post = factory.PostFactory.create()
        self.not_released_post = factory.PostFactory.create(
            slug='not-released-slug',
            release_time=timezone.now() + timezone.timedelta(hours=1)
        )


class PostViewTestCase(BaseTestCase):
    def test_get_post_correct_slug(self):
        response = self.client.get('/post/test-slug')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], self.post)
        self.assertTemplateUsed(response, 'post.html')

    def test_get_post_wrong_slug(self):
        response = self.client.get('/post/wrong-slug')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_get_post_unreleased(self):
        response = self.client.get('/post/not-released-slug')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')


class IndexViewTestCase(BaseTestCase):
    template = 'Index/index.html'
    path = ''

    def test_get_posts_non_empty_list(self):
        response = self.client.get(self.path)
        query = Post.objects.filter(release_time__lte=timezone.now())
        self.assertQuerysetEqual(response.context['post_list'], [repr(q) for q in query])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template)

    def test_get_posts_empty_list(self):
        Post.objects.all().delete()
        response = self.client.get(self.path)
        self.assertQuerysetEqual(response.context['post_list'], [])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template)

    def test_get_posts_only_not_released_posts(self):
        Post.objects.get(slug='test-slug').delete()
        response = self.client.get(self.path)
        self.assertQuerysetEqual(response.context['post_list'], [])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template)


class ArchiveViewTestCase(IndexViewTestCase):
    template = 'List/index_list.html'
    path = '/archiwum'


