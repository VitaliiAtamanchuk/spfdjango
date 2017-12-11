from django.conf.urls import url

from .views import blog_index, article_index

urlpatterns = [
    url(
        r'^$',
        blog_index,
        name='index'
    ),
    url(
        r'^article/(?P<pk>[\w-]+)/$',
        article_index,
        name='entry'
    ),
]