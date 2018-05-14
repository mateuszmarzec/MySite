
from django.test import Client, TestCase

from BlogAPI.tests import factory


class PostTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag = factory.TagFactory.create()
        self.post = factory.PostFactory.create()

    def test_get_post_correct_slug(self):
        response = self.client.get('/test-slug')
        self.assertEqual(response.status_code, 200)



