from django.conf.urls import url
from . import views

app_name = 'newblog'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('^post/(?P<pk>[0-9]+)/$',views.detail,name='detail')
]