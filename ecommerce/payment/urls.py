from django.conf.urls import url
from django.views.decorators.csrf import csrf_protect  
from . import views

urlpatterns = [
    url(r'^process/$', views.payment_process, name='process'),
    url(r'^done/$', csrf_protect(views.payment_done), name='done'),
    url(r'^canceled/$', csrf_protect(views.payment_canceled), name='canceled'),
]