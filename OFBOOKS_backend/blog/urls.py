from django.urls import path

from . import api

urlpatterns = [
    path('', api.get_feed, name='blog_feed'),
    path('tags/', api.trend_tags, name='trend_tags'),
    path('<uuid:id>/', api.blog_detail, name='blog_detail'),
    path('like/<uuid:id>/', api.like, name='like'),
    path('my/', api.myBlogs, name='my_blogs'),
]