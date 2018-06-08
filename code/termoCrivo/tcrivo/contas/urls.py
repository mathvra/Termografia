from django.conf.urls import url,include
from . import views

app_name='contas'

urlpatterns = [
    url(r'^cadastro/$', views.cadastro_view , name='cadastro'),
]