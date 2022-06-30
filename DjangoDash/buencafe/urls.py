from django.urls import path
from . import views

urlpatterns = [
    path('', views.buencafe, name='buencafe'),
    path('history', views.history, name='history'),
    path('coffee', views.coffee, name='coffee'),
    path('team', views.team, name='team'),
    path('eda', views.eda, name='eda'),
]
