from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(primary_key=True)
    view_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return '{}'.format(self.name)
