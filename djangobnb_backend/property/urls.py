from django.urls import path

from . import api

urlpatterns = [
    path('', api.properties_list, name='api-properties-list'),
    path('create/', api.create_property, name='api-create_property'),
]