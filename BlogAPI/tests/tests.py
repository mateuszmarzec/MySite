from django.utils import timezone
from django.test import Client, TestCase

from BlogAPI.tests import factory


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
        response = self.client.get('/test-slug')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], self.post)
        self.assertTemplateUsed(response, 'post.html')

    def test_get_post_wrong_slug(self):
        response = self.client.get('/wrong-slug')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_get_post_unreleased(self):
        response = self.client.get('/not-released-slug')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')


class IndexViewTestCase(BaseTestCase):
    pass
