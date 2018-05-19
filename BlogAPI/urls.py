"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from BlogAPI.views import IndexView, PostView, ArchiveView, TagSortingView, NewsletterView

urlpatterns = [
    path('', IndexView.as_view(), name=IndexView.name),
    path('archiwum', ArchiveView.as_view(), name=ArchiveView.name),
    path('newsletter', NewsletterView.as_view(), name=NewsletterView.name),
    path('post/<slug:slug>', PostView.as_view(), name=PostView.name),
    path('tag/<slug:tag>', TagSortingView.as_view(), name=TagSortingView.name),
]
