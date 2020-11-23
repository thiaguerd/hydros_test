from django.urls import path

from . import views

urlpatterns = [
    path('in', views.login, name='in'),
    path('out', views.out, name='out'),
    path('callback', views.callback, name='callback')
]
