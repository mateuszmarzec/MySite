# coding=utf-8
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.timezone import now
from django.views.generic import ListView, TemplateView, CreateView

from BlogAPI.forms import NewsletterForm
from BlogAPI.models.models import Post, Tag


class IndexView(TemplateView):
    name = 'index-view'
    template_name = 'Index/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'post_list': Post.objects.filter(release_time__lte=now())[:5],
            'tag_list': Tag.objects.all(),
        })
        return context


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
    template_name = 'List/index_list.html'

    def get_queryset(self):
        return Post.objects.filter(release_time__lte=now())


class TagSortingView(ListView):
    name = 'tag_sorting-view'
    template_name = 'List/index_list.html'

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs.get('tag'))
        return Post.objects.filter(release_time__lte=now(), tags=tag)


class NewsletterView(CreateView):
    name = 'newsletter-view'
    form_class = NewsletterForm
    template_name = 'newsletter.html'
    success_url = reverse_lazy('index-view')

    def form_valid(self, form):
        messages.success(self.request, message='Udało Ci się zapisać na Newsletter!', extra_tags='Gratuluję. ')
        return super(NewsletterView, self).form_valid(form)
