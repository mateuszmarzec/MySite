
from django.views.generic import ListView, TemplateView
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

from BlogAPI.models.models import Post, Tag


class IndexView(ListView):
    name = 'index-view'
    template_name = 'List/index.html'

    def get_queryset(self):
        return Post.objects.filter(release_time__lte=now()).order_by('create_time').reverse()[:5]


class PostView(TemplateView):
    name = 'post-view'
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, slug=kwargs.get('slug'), release_time__lte=now())
        tags = Tag.objects.filter(post=post)
        context.update({
            'post': post,
            'tags': tags,
        })
        return context


class ArchiveView(ListView):
    name = 'archive-view'
    template_name = 'Archiwum/archive.html'

    def get_queryset(self):
        return Post.objects.filter(release_time__lte=now()).order_by('create_time').reverse()
