"""Kota URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from MovieTheater import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/cinema/add/$', views.add_cinema),
    url(r'^api/showing/add/$', views.add_showing),
    url(r'^api/movie/add/$', views.add_movie),
    url(r'^api/cinema/$', views.get_all_cinema),
    url(r'^api/cinema/(?P<id>[^/]*)/$', views.get_cinema),
    url(r'^api/movie/$', views.get_all_movie),
    url(r'^api/movie/(?P<id>[^/]*)/$', views.get_movie),
    url(r'^api/showing/$', views.get_all_showing),
    url(r'^api/showing/(?P<id>[^/]*)/$', views.get_showing),
    url(r'^api/theater/$', views.get_all_theater),
    url(r'^api/theater/(?P<id>[^/]*)/$', views.get_theater),
    url(r'^api/ticket/$', views.get_all_ticket),
    url(r'^api/ticket/(?P<id>[^/]*)/$', views.get_ticket),
]
