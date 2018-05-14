from unittest import TestCase

from django.test import Client
from django.utils.timezone import now

from BlogAPI.tests import factory


class PostTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag = factory.TagFactory(name='test_tag')
        self.post = factory.PostFactory(
            title='test_title', slug='test-slug', tags=self.tag, create_time=now(),
            release_time=now(), text='test_text',
        )

    def test_get_post_correct_slug(self):
        response = self.client.get('/test-slug/')
        print(response)
