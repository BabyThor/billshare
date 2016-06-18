"""sharebill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from bills import views as bill_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^$',
        bill_views.Home.as_view(),
        name='home'
    ),
    url(
        r'^host/$',
        bill_views.Host.as_view(),
        name='host'
    ),
    url(
        r'^share/(?P<bill_id>\w+)$',
        bill_views.Share.as_view(),
        name='share'
    ),
    url(
        r'^friend/(?P<bill_id>\w+)$',
        bill_views.FriendView.as_view(),
        name='friend'
    ),
    url(
        r'^summary/(?P<bill_id>\w+)$',
        bill_views.SummaryView.as_view(),
        name='sumary'
    ),
]
