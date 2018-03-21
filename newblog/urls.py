from django.conf.urls import url
from . import views

app_name = 'newblog'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category')
]