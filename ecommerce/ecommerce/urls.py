["""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from shop import views

router = DefaultRouter()
router.register(r'shop', views.ShopViewSet, base_name='Product')

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('cart', include('cart.urls')),
                  path('orders/', include('orders.urls')),
                  path('', include('shop.urls')),
                  path('payment/', include(('payment.urls', 'payment'), namespace='payment')),
                  path('paypal/', include('paypal.standard.ipn.urls')),
                  path('shop/', include('shop.urls')),
                  path('api/', include(router.urls))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
