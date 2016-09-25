from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<command>(iostat|netstat -tulnp|uptime|who|ifconfig|free -m))/$', views.index_cmd, name='index_cmd'),
    url(r'^form$', views.index_form, name='index_form'),
]
