from django.conf.urls import url
from . import views

from paypal.standard.ipn import views as ipn_views

urlpatterns = [
    url(r'^process/$', views.payment_process
        , name='process'),
    url(r'^done/$', views.payment_done
        , name='done'),
    url(r'^canceled/$', views.payment_canceled
        , name='canceled'),
    url(r'^text/$', ipn_views.ipn)
]