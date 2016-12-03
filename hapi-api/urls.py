"""hapi-api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from hapifakenews.views import FakeNewsListVersion1ViewSet, FakeNewsRetrieveVersion1View, FakeNewsUrlCheckView
from hapisentiment.views import SentimentList
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from django.contrib import admin

#router.register(r'fakenews', FakeNewsList, base_name='asdf')
#router = DefaultRouter()
#router.register(r'fakenews/v1', FakeNewsListVersion1ViewSet)
#urlpatterns = router.urls

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #url(r'^', include(urlpatterns)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    #url('^fakenews', FakeNewsList.as_view()),
    url('^fakenews/v1/$', FakeNewsListVersion1ViewSet.as_view(), name='fakenewssitelist'),
    url(r'^fakenews/v1/(?P<pk>[0-9]+)/$', FakeNewsRetrieveVersion1View.as_view(), name='fakenewssitedetail'),
    url('^urlcheck/v1/(?P<url>.+)/$', FakeNewsUrlCheckView.as_view(), name='fakenewsurlcheck'),

#
#url('^hatespeech/', SentimentList.as_view()),

    
]    



