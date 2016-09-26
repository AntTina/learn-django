from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^cpu/',views.cpu,name='cpu'),
 	url(r'^cpuinfo/',views.cpu_info,name='cpuinfo'),
    url(r'^load/',views.load,name='load'),
    url(r'^loadinfo/',views.load_info,name='loadinfo'),
]
