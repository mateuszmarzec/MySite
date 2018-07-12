from django.test import Client, TestCase
from django.utils import timezone

from BlogAPI.tests import factory
from BlogAPI.models.models import Post
from BlogAPI.forms import NewsletterForm


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

    def test_get_posts_only_not_released_posts_empty_list(self):
        Post.objects.get(slug='test-slug').delete()
        response = self.client.get(self.path)
        self.assertQuerysetEqual(response.context['post_list'], [])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template)


class ArchiveViewTestCase(IndexViewTestCase):
    template = 'List/index_list.html'
    path = '/archiwum'


class TagSortingViewTestCase(IndexViewTestCase):
    template = 'List/index_list.html'
    path = '/tag/test-slug'

    def setUp(self):
        self.test_tag = factory.TagFactory.create(name='test_tag', slug='test-tag')
        super(TagSortingViewTestCase, self).setUp()

    def test_get_posts_non_empty_list_with_proper_tag(self):
        response = self.client.get(self.path)
        query = Post.objects.filter(release_time__lte=timezone.now(), tags=self.tag)
        self.assertQuerysetEqual(response.context['post_list'], [repr(q) for q in query])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template)

    def test_get_posts_empty_list(self):
        self.path = '/tag/test-tag'
        response = self.client.get(self.path)
        self.assertQuerysetEqual(response.context['post_list'], [])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.template)


class NewsletterViewTestCase(BaseTestCase):
    def test_get_form(self):
        response = self.client.get('/newsletter')
        self.assertTemplateUsed(response, 'newsletter.html')
        self.assertEqual(response.status_code, 200)

    def test_post_correct_data_with_name(self):
        data = {
            'first_name': 'TestName',
            'email': 'test@test.com',
            'agreement': True,
        }
        response = self.client.post(data=data, path='/newsletter')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_post_correct_data_without_name(self):
        data = {
            'email': 'test@test.com',
            'agreement': True,
        }
        response = self.client.post(data=data, path='/newsletter')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_post_incorrect_data_without_email(self):
        form = NewsletterForm(data={
            'first_name': 'TestName',
            'agreement': True,
        })
        response = self.client.post(data=form.data, path='/newsletter')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter.html')
