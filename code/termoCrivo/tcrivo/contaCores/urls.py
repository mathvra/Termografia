from django.conf.urls import url, include
from . import views

app_name='contaCores'

urlpatterns = [
    url(r'^$', views.contaCores, name="lista"),
    url(r'^(?P<nome>[\w-]+)/$', views.contaCores_detalhes, name="detalhes"),
]