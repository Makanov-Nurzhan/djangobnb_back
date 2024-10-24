from django.urls import path

from . import api

urlpatterns = [
    path('', api.properties_list, name='api-properties-list'),
    path('create/', api.create_property, name='api-create_property'),
    path('<uuid:pk>/', api.properties_detail, name='api_properties_detail'),
    path('<uuid:pk>/book/', api.book_property, name='api_book_property'),
]
