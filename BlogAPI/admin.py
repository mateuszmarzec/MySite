from django.contrib import admin

from BlogAPI.forms import PostForm
from BlogAPI.models.models import Tag, Post, NewsletterParticipant
from BlogAPI.models.models_site import Menu


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    ordering = ('-create_time',)
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'release_time')
    form = PostForm


class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'view_name', 'position')


class NewsletterParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'create_time')


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(NewsletterParticipant, NewsletterParticipantAdmin)
