from django.urls import path

from apps.tours.views import hello_view, goodbye_view

urlpatterns = [
    path('hello/', hello_view),
    path('goodbye/',goodbye_view),
]