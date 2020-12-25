# apps/blog/urls.py

from django.urls import path
from .views import home, general, programming, tutorial, technology, videogame

urlpatterns = [
    path('', home, name='index'),
    path('general/', general, name='general'),
    path('programming/', programming, name='programming'),
    path('tutorial/', tutorial, name='tutorial'),
    path('technology/', technology, name='technology'),
    path('videogame/', videogame, name='videogame'),
]
