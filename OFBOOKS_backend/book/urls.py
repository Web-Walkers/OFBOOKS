from django.urls import path

from . import api

urlpatterns = [
    path('', api.get_feed, name='get_feed'),
    path('subjects/', api.get_subjects, name='get_subjects'),
    path('subject/<uuid:id>/', api.subject_detail, name='subject_detail'),
    path('best-subjects/', api.get_best_subjects, name='get_best_subjects'),
    path('publishers/', api.get_publishers, name='get_publishers'),
    path('publisher/<uuid:id>/', api.publisher_detail, name='publisher_detail'),
    path('literatures/', api.get_literatures, name='get_literatures'),
    path('literature/<uuid:id>/', api.literature_detail, name='literature_detail'),
    path('<uuid:id>/', api.book_detail, name='book_detail'),
]